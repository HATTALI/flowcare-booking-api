from pathlib import Path

from fastapi import FastAPI

from app.core.config import settings


app = FastAPI(title=settings.app_name)


def ensure_upload_directories() -> None:
    Path(settings.upload_dir).mkdir(parents=True, exist_ok=True)
    Path(settings.customer_id_dir).mkdir(parents=True, exist_ok=True)
    Path(settings.attachment_dir).mkdir(parents=True, exist_ok=True)


@app.on_event("startup")
def on_startup() -> None:
    ensure_upload_directories()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": f"{settings.app_name} is running"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}