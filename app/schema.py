from pydantic import BaseModel


class Document(BaseModel):
    count: int
    email: str
