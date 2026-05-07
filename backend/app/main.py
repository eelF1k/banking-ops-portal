from fastapi import FastAPI

from app.api.v1.router import router as v1_router
from app.core.settings import settings

app = FastAPI(title=settings.app_name)

app.include_router(v1_router, prefix="/api/v1")


@app.get("/")
def root():
    return {"service": settings.app_name, "env": settings.app_env}
