from typing import List, Optional
from sqlalchemy.orm import Session
from database.molecules import MoleculeModel
from ..models.molecule import MoleculeCreate, Molecule

class MoleculeService:
    def __init__(self):
        self.has_rdkit = False
        try:
            import rdkit
            self.has_rdkit = True
        except ImportError:
            print("Warning: RDKit not installed. Some molecular features will be limited.")

    async def get_all_molecules(self, db: Session) -> List[Molecule]:
        molecules = db.query(MoleculeModel).all()
        return [Molecule.from_orm(molecule) for molecule in molecules]

    async def get_molecule(self, db: Session, molecule_id: int) -> Optional[Molecule]:
        molecule = db.query(MoleculeModel).filter(MoleculeModel.id == molecule_id).first()
        if molecule:
            return Molecule.from_orm(molecule)
        return None

    async def create_molecule(self, db: Session, molecule: MoleculeCreate) -> Molecule:
        molecular_weight = 0.0
        
        if self.has_rdkit:
            from rdkit import Chem
            from rdkit.Chem import Descriptors
            
            mol = Chem.MolFromSmiles(molecule.smiles)
            if not mol:
                raise ValueError("Invalid SMILES notation")
            
            molecular_weight = Descriptors.ExactMolWt(mol)

        db_molecule = MoleculeModel(
            name=molecule.name,
            formula=molecule.formula,
            smiles=molecule.smiles,
            molecular_weight=molecular_weight
        )
        
        db.add(db_molecule)
        db.commit()
        db.refresh(db_molecule)
        
        return Molecule.from_orm(db_molecule)
    
    async def search_molecules(
        self, 
        db: Session, 
        name: Optional[str] = None,
        formula: Optional[str] = None,
        min_weight: Optional[float] = None,
        max_weight: Optional[float] = None
    ) -> List[Molecule]:
        query = db.query(MoleculeModel)
        
        if name:
            query = query.filter(MoleculeModel.name.ilike(f"%{name}%"))
        if formula:
            query = query.filter(MoleculeModel.formula == formula)
        if min_weight is not None:
            query = query.filter(MoleculeModel.molecular_weight >= min_weight)
        if max_weight is not None:
            query = query.filter(MoleculeModel.molecular_weight <= max_weight)
            
        molecules = query.all()
        return [Molecule.from_orm(m) for m in molecules]