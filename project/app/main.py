from fastapi import Depends, FastAPI

from app.config import Settings, get_Settings

app = FastAPI()


@app.get("/ping")
async def pong(settings: Settings = Depends(get_Settings)):  # noqa: B008
    return {"ping": "pong", "environment": settings.environment, "testing": settings.testing}
