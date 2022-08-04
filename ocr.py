import pytesseract
import asyncio

async def read_image(img_path,lang='eng'):
    try:
        text = pytesseract.image_to_string(img_path,lang)
        await asyncio.sleep(2)
        return text
    except:
        return "Error Processing file"

