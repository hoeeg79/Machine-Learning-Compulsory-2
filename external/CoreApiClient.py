import requests
from typing import List, Dict, Optional


class CoreApiClient:
    BASE_URL = "https://api.core.ac.uk/v3/search/works"

    def __init__(self, api_key: str):
        self.headers = {
            "Authorization": f"Bearer {api_key}"
        }

    def search_works(
            self,
            query: str = "_exists_:doi",
            limit: int = 10,
            offset: int = 0
    ) -> List[Dict]:
        """
        Søg efter works i CORE API.

        :param query: Søgeterm, fx "smoking" eller "_exists_:doi"
        :param limit: Antal resultater at returnere
        :param offset: Startposition (til pagination)
        :return: Liste af artikler som dict
        """
        params = {
            "q": query,
            "limit": limit,
            "offset": offset
        }

        response = requests.get(self.BASE_URL, headers=self.headers, params=params)

        if response.status_code != 200:
            raise Exception(f"CORE API request failed: {response.status_code} - {response.text}")

        data = response.json()
        results = data.get("results", [])
        return results


# -------------------------
# Eksempel på brug
# -------------------------

if __name__ == "__main__":
    API_KEY = "DIN_CORE_API_KEY_HER"

    client = CoreApiClient(API_KEY)

    # Søger efter artikler med DOI
    works = client.search_works(query="smoking", limit=5)

    for i, work in enumerate(works, start=1):
        title = work.get("title")
        authors = ", ".join(work.get("authors", []))
        doi = work.get("doi")
        year = work.get("yearPublished")
        print(f"{i}. {title} ({year}) by {authors} - DOI: {doi}")
