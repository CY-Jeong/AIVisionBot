from fastapi import APIRouter

router = APIRouter(
    prefix="/",
    tags=["index"],
    responses={200: {"description": "OK"}}
)s

@router.get("/")
async def index() -> dict:
    return {"AI_Vision_Ready": True}