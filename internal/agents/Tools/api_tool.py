import os
from typing import List

from dotenv import load_dotenv

from external.CoreApiClient import CoreApiClient
from models.core_models import CoreWork

load_dotenv()

# Hent API nøgle fra miljøvariabel
API_KEY = os.getenv("API_KEY")

def call_api_tool(query: str) -> List[CoreWork]:
    """
    Kalder CORE API og returnerer en liste af CoreWork-objekter.
    Tilføjer fullText som chunks til hvert objekt.
    """
    client = CoreApiClient(API_KEY)
    response = client.search_works(query=query)
    results: List[CoreWork] = []

    for res in response:
        text_chunks = split_text(res.fullText, chunk_size=500)

        # Tilføj en ny attribut til objektet til chunks
        res.fullText = text_chunks[0]

        # convert pydantic model -> dict
        results.append(res.model_dump()) 
    
    return results


def split_text(text: str, chunk_size: int = 50) -> List[str]:
    """
    Deler teksten op i bidder af chunk_size tegn.
    """
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
