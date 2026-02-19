from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import health, root

app = FastAPI(
    title="Cullenia AI API",
    description="FastAPI application for Cullenia AI",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(root.router)
app.include_router(health.router)
