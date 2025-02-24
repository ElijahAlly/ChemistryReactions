from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_reactions():
    return {"message": "Reactions endpoint coming soon"}
