from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ElementBase(BaseModel):
    atomic_number: int
    symbol: str
    name: str
    group: str
    period: int
    block: str
    atomic_weight: float
    density: Optional[float] = None
    melting_point: Optional[float] = None
    boiling_point: Optional[float] = None
    specific_heat: Optional[float] = None
    electronegativity: Optional[float] = None
    abundance: Optional[float] = None
    origin: str
    phase: str

class ElementCreate(ElementBase):
    pass

class Element(ElementBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True