from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_simulations():
    return {"message": "Simulations endpoint coming soon"}
