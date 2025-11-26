import os

from dotenv import load_dotenv

from external.CoreApiClient import CoreApiClient

load_dotenv()

# Hent API nøgle fra miljøvariabel
API_KEY = os.getenv("API_KEY")

def call_api_tool(query: str):
    client = CoreApiClient(API_KEY)
    response = client.search_works(query=query)
    return response