from fastapi import FastAPI, UploadFile, File, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from pydantic import BaseModel

import clamd
import os

app = FastAPI()

# Set up Jinja2 for HTML rendering
templates = Jinja2Templates(directory="templates")

# Connect to ClamAV running in Docker
cd = clamd.ClamdNetworkSocket(
    host=os.getenv("CLAMD_HOST", "localhost"),
    port=int(os.getenv("CLAMD_PORT", 3310))
)

class ScanResult(BaseModel):
    filename: str
    result: dict

@app.get("/", response_class=HTMLResponse)
async def form(request: Request):
    """
    Renders the upload form HTML page.
    
    Args:
        request (Request): The incoming FastAPI request object.
    
    Returns:
        TemplateResponse: HTML response containing the upload form page.
    """
    return templates.TemplateResponse("upload.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def upload(request: Request, file: UploadFile = File(...)):
    result = cd.instream(file.file)
    status = "clean"
    if result['stream'][0] != "OK":
        status = "infected"
    return templates.TemplateResponse("upload.html", {
        "request": request,
        "filename": file.filename,
        "status": status,
        "scan_result": result
    })

@app.post("/scan", response_model=ScanResult)
async def scan_file(file: UploadFile = File(...)):
    result = cd.instream(file.file)

    return ScanResult(
        filename=file.filename,
        result=result
    )