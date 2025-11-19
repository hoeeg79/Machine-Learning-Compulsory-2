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
