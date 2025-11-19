import requests
from typing import Type, TypeVar, List

from pydantic import BaseModel

from models.core_models import CoreWork

T = TypeVar("T", bound=BaseModel)

class CoreApiClient:
    BASE_URL = "https://api.core.ac.uk/v3/search/works"

    def __init__(self, api_key: str):
        self.headers = {"Authorization": f"Bearer {api_key}"}

    def search_works(self, query: str = "_exists_:doi", limit: int = 10, offset: int = 0, model: Type[T] = CoreWork) -> List[T]:
        """
        Søgning i CORE API og returnér en liste af Pydantic-modeller.
        """
        params = {"q": query, "limit": limit, "offset": offset}
        response = requests.get(self.BASE_URL, headers=self.headers, params=params)
        response.raise_for_status()
        data = response.json()
        results = data.get("results", [])
        return [model.parse_obj(r) for r in results]