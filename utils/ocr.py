import pyautogui
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = pyautogui.screenshot() # takes the screenshot and stores in img

text = pytesseract.image_to_string(img) # image to text now

print(text)