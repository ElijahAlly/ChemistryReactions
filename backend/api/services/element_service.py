from typing import List, Optional
from sqlalchemy.orm import Session
from database.elements import ElementModel
from ..models.element import Element

class ElementService:
    def __init__(self):
        self.has_rdkit = False
        try:
            import rdkit
            self.has_rdkit = True
        except ImportError:
            print("Warning: RDKit not installed. Some elemental features will be limited.")

    async def get_all_elements(self, db: Session) -> List[Element]:
        elements = db.query(ElementModel).all()
        return [Element.from_orm(element) for element in elements]

    async def get_element(self, db: Session, element_id: int) -> Optional[Element]:
        element = db.query(ElementModel).filter(ElementModel.id == element_id).first()
        if element:
            return Element.from_orm(element)
        return None
    
    async def search_elements(
        self, 
        db: Session, 
        name: Optional[str] = None
    ) -> List[Element]:
        query = db.query(ElementModel)
        
        if name:
            query = query.filter(ElementModel.name.ilike(f"%{name}%"))
            
        elements = query.all()
        return [Element.from_orm(m) for m in elements]