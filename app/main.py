import os
from pathlib import Path

from fastapi import FastAPI

app = FastAPI(title="Lab Hello App")

GREETING = os.getenv("GREETING", "Hello from Databricks Apps")
APP_NAME = os.getenv("DATABRICKS_APP_NAME", "local")
VERSION_FILE = Path(__file__).parent / "version.txt"


def read_version() -> str:
    # CI writes the commit SHA here before deploying; local runs have no file.
    return VERSION_FILE.read_text().strip() if VERSION_FILE.exists() else "local"


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/")
def home() -> dict[str, str | bool]:
    return {
        "message": GREETING,
        "app": APP_NAME,
        "version": read_version(),
        # Never echo secret values; only report whether one was injected.
        "secretConfigured": bool(os.getenv("DEMO_SECRET")),
    }
