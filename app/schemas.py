from pydantic import BaseModel, ValidationError
from typing import Optional

class Qiuz(BaseModel):
    id: int
    question: str
    answer: str
    creation_date: str

    class Config:
        orm_mode = True

