from pydantic import BaseModel
from typing import Optional

class Country(BaseModel):
    id: int
    code: str
    name: str

class State(BaseModel):
    id: int
    name: str
    country_id: Optional[int] = None # Assuming country_id might be null if Nigeria not found

class LGA(BaseModel):
    id: int
    state_id: int
    name: str