import json
import os
from typing import Any, Dict, List

from dotenv import load_dotenv
from mistralai import ToolMessage, TextChunk

from external.CoreApiClient import CoreApiClient
from models.core_models import CoreWork

load_dotenv()

# Hent API nøgle fra miljøvariabel
API_KEY = os.getenv("API_KEY")


def call_api_tool(query: str) -> ToolMessage:
    client = CoreApiClient(API_KEY)
    response = client.search_works(query=query)

    results: List[Dict[str, Any]] = []
    for res in response:
        # mutate model if you want
        res.fullText = (res.fullText or "")[:500]

        # convert pydantic model -> dict
        results.append(res.model_dump())   # ✅ Pydantic v2
        # if you're on pydantic v1, use: res.dict()

    return results
