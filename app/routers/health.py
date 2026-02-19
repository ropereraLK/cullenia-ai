from fastapi import APIRouter

from app.config import get_config

router = APIRouter(tags=["health"])


@router.get("/health")
def health():
    config = get_config()
    return {"status": "up", "version": config.version}
