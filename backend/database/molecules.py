from sqlalchemy import Column, String, Float
from .base import BaseModel

class MoleculeModel(BaseModel):
    __tablename__ = "molecules"

    name = Column(String, index=True)
    formula = Column(String)
    smiles = Column(String)
    molecular_weight = Column(Float)