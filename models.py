from pydantic import BaseModel, Field
from typing import Optional


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)  # GraterThen >=0 && LessThen<=5
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "Author Name",
                "description": "A book description",
                "rating": 5
            }
        }
    }