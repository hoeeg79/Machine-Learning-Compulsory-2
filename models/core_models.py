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
    depositedDate: Optional[str]
    fullText: Optional[str]
