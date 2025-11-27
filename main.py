import os
from typing import List

from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
import autogen

from external.CoreApiClient import CoreApiClient
from internal.agents import critic_agent
from internal.agents import search_agent
from internal.agents import summarize_agent
from internal.agents import user_proxy_agent
from internal.agents.Tools.api_tool import call_api_tool
from models.core_models import CoreWork

app = FastAPI()


# Load .env filen
load_dotenv()

# Hent API nøgle fra miljøvariabel
API_KEY = os.getenv("API_KEY")
AI_API_KEY = os.getenv("AI_API_KEY")

if not API_KEY:
    raise ValueError("API_KEY is not set in environment variables!")

if not AI_API_KEY:
    raise ValueError("AI_API_KEY is not set in environment variables!")

# -------- DTO --------
class SearchPaperRequest(BaseModel):
    topic: str
    year_constraint: str   # "in", "before", "after"
    year: int
    min_citations: int


# -------- Endpoint --------
@app.post("/searchpaper")
async def search_paper(dto: SearchPaperRequest):
    """
    Endpoint der modtager en DTO og returnerer den (eller hvad du vil gøre med den).
    """
    # todo Lav en prompt ud fra json body
    # todo aflever prompt til agent
    await start_group_agents(dto)
    return {
        "message": "DTO modtaget",
        "data": dto
    }

LLM_CEREBRAS_CONFIG = {
    "config_list": [
        {
            "model": "llama-3.3-70b",
            "api_key": AI_API_KEY,
            "api_type": "cerebras",
            "max_tokens": 10000,
            "seed": 1234,
            "stream": False,
            "temperature": 0.0,
        }
    ]
}

LLM_MISTRAL_CONFIG = {
    "config_list": [
        {
            "model": "open-mistral-nemo-2407",
            "api_key": AI_API_KEY,
            "api_type": "mistral",
            "api_rate_limit": 0.25,
            "repeat_penalty": 1.1,
            "temperature": 0.0,
            "seed": 42,
            "stream": False,
            "native_tool_calls": False,
            "cache_seed": None,
        }
    ]
}

async def start_group_agents(dto: SearchPaperRequest):
    critic = critic_agent.create_critic_agent(LLM_CEREBRAS_CONFIG)
    search = search_agent.create_search_agent(LLM_CEREBRAS_CONFIG)
    summarize = summarize_agent.create_summarize_agent(LLM_CEREBRAS_CONFIG)
    user_proxy = user_proxy_agent.create_user_proxy()

    group = autogen.GroupChat(
        agents=[search, critic, summarize, user_proxy],
        messages=[],
        max_round=10,
        speaker_selection_method="auto",
        send_introductions=True,
        allow_repeat_speaker=False,
        role_for_select_speaker_messages="assistant", 
    )

    manager = autogen.GroupChatManager(
        groupchat=group,
        llm_config=LLM_CEREBRAS_CONFIG,
        is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"]
    )

    user_proxy.initiate_chat(
        manager,
        message=(
            "Task: Search for academic papers on the topic: "f"{dto.topic}, "
            f"with a year constraint: {dto.year_constraint} {dto.year}, "
            f"and a minimum of {dto.min_citations} citations."
            "Make sure that the papers are relevant and meet the criteria."
        ),
        summary_method="reflection_with_llm"
    )




# todo eksempel på brug af core klienten
"""
API_KEY = "DIN_CORE_API_KEY_HER"
client = CoreApiClient(API_KEY)

# Hent 5 artikler om "smoking" og parse direkte til CoreWork
works: List[CoreWork] = client.search_works(query="smoking", limit=5)

for work in works:
    print(f"{work.title} ({work.yearPublished}) - DOI: {work.doi}")
"""




def get_core_client() -> CoreApiClient:
    if not API_KEY:
        raise RuntimeError("CORE_API_KEY is missing in environment variables")
    return CoreApiClient(api_key=API_KEY)



@app.get("/core/search", response_model=List[CoreWork])
def search_core_works(
    query: str = "_exists_:doi",
):
    """
    Endpoint der søger i CORE API og returnerer en liste CoreWork-modeller.
    """
    try:
        return call_api_tool(query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))