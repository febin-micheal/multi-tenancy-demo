from fastapi import APIRouter

router = APIRouter(
    prefix="/tests",
    tags=["tests"],
)


@router.get("/hello")
async def hello_world():
    """
    Sample 'hello, world' test
    """
    return {"message": "Hello, World"}
