from fastapi import APIRouter

router = APIRouter(tags=["root"])


@router.get("/")
async def root():
    return {"message": "Welcome to Cullenia AI API"}
