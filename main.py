from fastapi import FastAPI,File,UploadFile
from typing import List
import time
import asyncio
import ocr
import utils

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Visit the endpoint: /api/v1/extract_text to perform OCR."}

@app.post("/api/v1/extract_text")
async def get_text(Images: List[UploadFile]=File(...)):
    response ={}
    for img in Images:
        temp_file =utils.get_filepath_from_server(img,path="./",save_as=img.filename)
        extracted_text =await ocr.read_image(temp_file)
        response[img.filename]=extracted_text

    return response
    