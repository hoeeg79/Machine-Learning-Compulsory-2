import os
from typing import List

from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
import autogen

from external.CoreApiClient import CoreApiClient
from internal.agents import critic_agent
from internal.agents import search_agent
from internal.agents import user_proxy_agent
from models.core_models import CoreWork

app = FastAPI()


# Load .env filen
load_dotenv()

# !!! HAR JEG IMPORTERET DENNE KORREKT INDE I api_tool.py? !!!
# Hent API nøgle fra miljøvariabel
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY is not set in environment variables!")


# -------- DTO --------
class SearchPaperRequest(BaseModel):
    topic: str
    year_constraint: str   # "in", "before", "after"
    year: int
    min_citations: int


# -------- Endpoint --------
@app.post("/searchpaper")
def search_paper(dto: SearchPaperRequest):
    """
    Endpoint der modtager en DTO og returnerer den (eller hvad du vil gøre med den).
    """
    # todo Lav en prompt ud fra json body
    # todo aflever prompt til agent

    return {
        "message": "DTO modtaget",
        "data": dto
    }

def start_group_agents(dto: SearchPaperRequest):
    critic = critic_agent.create_critic_agent()
    search = search_agent.create_search_agent(LLM_CONFIG)
    user_proxy = user_proxy_agent.create_user_proxy()

    group = autogen.GroupChat(
        agents=[critic, search, user_proxy],
        messages=[],
        max_round=50,
        speaker_selection_method="auto"
    )

    manager = autogen.GroupChatManager(
        groupchat=group,
        llm_config=LLM_CONFIG
    )

    user_proxy.initiate_chat(
        manager=manager,
        message=(
            "Task: Search for academic papers on the topic: "f"{dto.topic}, "
            f"with a year constraint: {dto.year_constraint} {dto.year}, "
            f"and a minimum of {dto.min_citations} citations."
            "Make sure that the papers are relevant and meet the criteria."
            "Stop when you have found suitable papers and print 'TERMINATE'."
        )
    )

LLM_CONFIG = {
    "config_list": [
        {
            "model": "open-mistral-nemo",
            "api_key": "[YOUR_API_KEY]",
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
    limit: int = 10,
    offset: int = 0,
    client: CoreApiClient = Depends(get_core_client)
):
    """
    Endpoint der søger i CORE API og returnerer en liste CoreWork-modeller.
    """
    try:
        return client.search_works(query=query, limit=limit, offset=offset)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))