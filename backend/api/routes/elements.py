from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List, Optional
from sqlalchemy.orm import Session
from database.database import get_db
from ..models.element import Element
from ..services.element_service import ElementService

router = APIRouter()
element_service = ElementService()

@router.get("/", response_model=List[Element])
async def get_elements(db: Session = Depends(get_db)):
    print("Getting all elements")
    return await element_service.get_all_elements(db)

@router.get("/{element_id}", response_model=Element)
async def get_element(element_id: int, db: Session = Depends(get_db)):
    element = await element_service.get_element(db, element_id)
    if not element:
        raise HTTPException(status_code=404, detail="Element not found")
    return element

# @router.post("/", response_model=Element)
# async def create_element(element: ElementCreate, db: Session = Depends(get_db)):
#     return await element_service.create_element(db, element)

@router.get("/search/", response_model=List[Element])
async def search_elements(
    name: Optional[str] = Query(default=None),
    db: Session = Depends(get_db)
):
    """Search elements by various criteria"""
    return await element_service.search_elements(db, name)
