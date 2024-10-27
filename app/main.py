from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import easyocr

app = FastAPI()
reader = easyocr.Reader(['en'], gpu=False)


@app.post("/ocr")
async def ocr_endpoint(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()

        results = reader.readtext(image_bytes)

        text = " ".join([result[1] for result in results])

        return JSONResponse(content={"text": text})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
