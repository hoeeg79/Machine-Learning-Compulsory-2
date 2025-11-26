from typing import List, Optional
from pydantic import BaseModel

class Identifier(BaseModel):
    identifier: str
    type: str

class DataProvider(BaseModel):
    id: Optional[int]
    name: Optional[str]
    url: Optional[str]
    logo: Optional[str]

class Link(BaseModel):
    type: str
    url: str

class Language(BaseModel):
    code: str
    name: str


class Author(BaseModel):
    name: str


class CoreWork(BaseModel):
    id: int
    title: str
    authors: Optional[List[Author]] = None
    yearPublished: Optional[int]
    doi: Optional[str]
    description: Optional[str] = None
    downloadUrl: Optional[str]
    depositedDate: Optional[str]
    arxivId: Optional[str]
    citationCount: Optional[int]
    documentType: Optional[str]
    contributors: List[str] = []
    fieldOfStudy: Optional[str]
    magId: Optional[str]
    pubmedId: Optional[str]
    oaiIds: List[str] = []
    outputs: List[str] = []
    sourceFulltextUrls: List[str] = []
    language: Optional[Language]
    dataProviders: List[DataProvider] = []
    identifiers: List[Identifier] = []
    links: List[Link] = []
    fullText: Optional[str]
