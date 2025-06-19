from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import clamd
import os

app = FastAPI()

# Connect to ClamAV running in Docker
cd = clamd.ClamdNetworkSocket(
    host=os.getenv("CLAMD_HOST", "localhost"),
    port=int(os.getenv("CLAMD_PORT", 3310))
)

class ScanResult(BaseModel):
    filename: str
    status: str  # "clean" or "infected"
    raw: dict

@app.post("/scan", response_model=ScanResult)
async def scan_file(file: UploadFile = File(...)):
    result = cd.instream(file.file)
    status = "clean"
    for _, (_, virus_name) in result.items():
        if virus_name != "OK":
            status = "infected"
            break
    return ScanResult(
        filename=file.filename,
        status=status,
        raw=result
    )