import os
from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import clamd

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Connect to the ClamAV daemon (running in Docker)
cd = clamd.ClamdNetworkSocket(
    host=os.getenv("CLAMD_HOST", "localhost"),
    port=int(os.getenv("CLAMD_PORT", 3310))
)
@app.get("/", response_class=HTMLResponse)
def form(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def upload(request: Request, file: UploadFile = File(...)):
    result = cd.instream(file.file)
    status = 'clean'
    if result['stream'][0] != 'OK':
        status = 'infected'
    return templates.TemplateResponse("upload.html", {
        "request": request,
        "filename": file.filename,
        "status": status,
        "scan_result": result
    })