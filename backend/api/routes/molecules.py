from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List, Optional
from sqlalchemy.orm import Session
from database.database import get_db
from ..models.molecule import Molecule, MoleculeCreate, MoleculeProperties
from ..services.molecule_service import MoleculeService
from ..services.molecule_operations import MoleculeOperations

router = APIRouter()
molecule_service = MoleculeService()
molecule_ops = MoleculeOperations()

@router.get("/", response_model=List[Molecule])
async def get_molecules(db: Session = Depends(get_db)):
    return await molecule_service.get_all_molecules(db)

@router.get("/{molecule_id}", response_model=Molecule)
async def get_molecule(molecule_id: int, db: Session = Depends(get_db)):
    molecule = await molecule_service.get_molecule(db, molecule_id)
    if not molecule:
        raise HTTPException(status_code=404, detail="Molecule not found")
    return molecule

@router.post("/", response_model=Molecule)
async def create_molecule(molecule: MoleculeCreate, db: Session = Depends(get_db)):
    return await molecule_service.create_molecule(db, molecule)

@router.get("/search/", response_model=List[Molecule])
async def search_molecules(
    name: Optional[str] = Query(default=None),
    formula: Optional[str] = Query(default=None),
    min_weight: Optional[float] = Query(default=None),
    max_weight: Optional[float] = Query(default=None),
    db: Session = Depends(get_db)
):
    """Search molecules by various criteria"""
    return await molecule_service.search_molecules(db, name, formula, min_weight, max_weight)

@router.get("/{molecule_id}/properties", response_model=MoleculeProperties)
async def get_molecule_properties(molecule_id: int, db: Session = Depends(get_db)):
    """Get detailed properties of a molecule"""
    molecule = await molecule_service.get_molecule(db, molecule_id)
    if not molecule:
        raise HTTPException(status_code=404, detail="Molecule not found")
    
    properties = molecule_ops.get_molecular_properties(molecule.smiles)
    return MoleculeProperties(**properties)