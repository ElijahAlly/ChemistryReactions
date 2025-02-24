from rdkit import Chem
from typing import Optional, Dict

class MoleculeOperations:
    @staticmethod
    def validate_molecular_formula(formula: str) -> bool:
        """Validate if a molecular formula is properly formatted"""
        import re
        pattern = r'^([A-Z][a-z]?\d*)*$'
        return bool(re.match(pattern, formula))

    @staticmethod
    def calculate_mass(formula: str) -> Optional[float]:
        """Calculate molecular mass from formula"""
        atomic_masses = {
            'H': 1.008, 'C': 12.011, 'N': 14.007, 'O': 15.999,
            'F': 18.998, 'P': 30.974, 'S': 32.065, 'Cl': 35.453
        }
        
        try:
            import re
            pattern = r'([A-Z][a-z]?)(\d*)'
            matches = re.findall(pattern, formula)
            
            total_mass = 0
            for element, count in matches:
                count = int(count) if count else 1
                if element not in atomic_masses:
                    return None
                total_mass += atomic_masses[element] * count
                
            return round(total_mass, 3)
        except:
            return None

    @staticmethod
    def get_molecular_properties(smiles: str) -> Dict:
        """Get molecular properties using RDKit"""
        try:
            mol = Chem.MolFromSmiles(smiles)
            if not mol:
                return {}
            
            from rdkit.Chem import Descriptors, Draw
            return {
                'molecular_weight': round(Descriptors.ExactMolWt(mol), 3),
                'logp': round(Descriptors.MolLogP(mol), 2),
                'polar_surface_area': round(Descriptors.TPSA(mol), 2),
                'rotatable_bonds': Descriptors.NumRotatableBonds(mol),
                'h_bond_donors': Descriptors.NumHDonors(mol),
                'h_bond_acceptors': Descriptors.NumHAcceptors(mol)
            }
        except:
            return {}
