# tasks.py

from celery import shared_task
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@shared_task
def convert(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text
