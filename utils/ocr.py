from PIL import ImageEnhance, ImageFilter
import pytesseract
import pyautogui
import time
from datetime import datetime

#just needed for pytesseract to work, it needs its root file path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

ocr_log = {}

def txt():
    img = pyautogui.screenshot().convert("RGB") # takes the screenshot and stores in img and makes the colour rgb which tesseract expects
    img = img.convert("L")
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0)
    img = img.filter(ImageFilter.SHARPEN)
    img = img.resize((img.width * 2, img.height * 2))
    text = pytesseract.image_to_string(img) # image to text now
    return text

i = 0
while(i<3):
    timestamp = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) # makes a time stamp
    text = txt()
    d_timestamp_text = {timestamp: text}
    ocr_log.update(d_timestamp_text)

    print(f"[{timestamp}] Captured text: {text}...")  # Print preview of text

    time.sleep(5)
    i+=1

# this function is just so that i can export ocr_log in summarizer.py
def get_ocr_log():
    return ocr_log
