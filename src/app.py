import loggings
from src.router.status_router import router as status_router
from src.router.index_router import router as index_router
from fastapi import FastAPI

app = FastAPI(
    title="AI Vision Manager",
    description="AI tools",
    version="1.0.0",
    openapi_url="/docs/openapi.json"
)

app.include_router(
    index_router
)
