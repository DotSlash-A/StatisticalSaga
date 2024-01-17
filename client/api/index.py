import base64
import requests

from typing import Optional
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Header, File, UploadFile, HTTPException

app = FastAPI()

def validate_api_key(api_key: Optional[str] = Header(None)) -> None:
  if api_key is None:
    raise HTTPException(status_code = 400, detail = "OpenAI API key missing! 🙄")

@app.get("/api", description = "API Health check endpoint ❤️‍🩹")
def hello_world():
  return { "docs": "/api/docs" }

