import os

from external.CoreApiClient import CoreApiClient
from main import API_KEY

def call_api_tool(query: str):
    client = CoreApiClient(API_KEY)
    response = client.search_works(query=query)
    return response