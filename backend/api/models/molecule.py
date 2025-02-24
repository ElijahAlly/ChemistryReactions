from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MoleculeBase(BaseModel):
    name: str
    formula: str
    smiles: str  # SMILES notation for molecular structure
    molecular_weight: float

class MoleculeCreate(MoleculeBase):
    pass

# Add this new class
class MoleculeProperties(BaseModel):
    logp: Optional[float] = None
    polar_surface_area: Optional[float] = None
    rotatable_bonds: Optional[int] = None
    h_bond_donors: Optional[int] = None
    h_bond_acceptors: Optional[int] = None

class Molecule(MoleculeBase):
    id: int
    properties: Optional[MoleculeProperties] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True