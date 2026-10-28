
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Compiler Voice Assistant API")

allowed_origins = [
    origin.strip()
    for origin in os.getenv("ALLOWED_ORIGINS", "").split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Authorization"],
)


class CommandRequest(BaseModel):
    text: str


@app.get("/")
def root():
    return {
        "name": "Compiler Voice Assistant API",
        "status": "online",
        "mode": "safe web prototype",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/command")
def command(request: CommandRequest):
    text = request.text.strip()

    if not text:
        return {"status": "error", "message": "Please enter a command."}

    return {
        "status": "received",
        "message": "Command received. Execution is not enabled yet.",
        "text": text,
    }
