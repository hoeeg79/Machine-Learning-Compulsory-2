from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


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
