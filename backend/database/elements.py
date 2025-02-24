from sqlalchemy import Column, Integer, String, Float
from .base import BaseModel

class ElementModel(BaseModel):
    __tablename__ = "elements"

    atomic_number = Column(Integer, unique=True, index=True)
    symbol = Column(String, unique=True, index=True)
    name = Column(String, unique=True)
    group = Column(String)
    period = Column(Integer)
    block = Column(String)
    atomic_weight = Column(Float)
    density = Column(Float, nullable=True)
    melting_point = Column(Float, nullable=True)
    boiling_point = Column(Float, nullable=True)
    specific_heat = Column(Float, nullable=True)
    electronegativity = Column(Float, nullable=True)
    abundance = Column(Float, nullable=True)
    origin = Column(String)
    phase = Column(String)
    