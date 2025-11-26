import json
import os
from typing import List

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

    chunks = []
    for res in response:
        text_chunks = split_text(res.fullText, chunk_size=50)
        first_chunk = text_chunks[0] if text_chunks else ""
        chunks.append(TextChunk(text=f"{res.title} ({res.yearPublished})\n{first_chunk}"))

    return ToolMessage(
        content=chunks,
        tool_name="api_tool"
    )


def split_text(text: str, chunk_size: int = 50) -> List[str]:
    """
    Deler teksten op i bidder af chunk_size tegn.
    """
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
