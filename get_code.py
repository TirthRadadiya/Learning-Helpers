import pyperclip
import pytesseract
from PIL import ImageGrab
import time
import keyboard

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# s1 = "Hello world"
# pyperclip.copy(s1)
# s2 = pyperclip.paste()

def work():
    try:
        img = ImageGrab.grabclipboard()
        if img:
            text = pytesseract.image_to_string(img)
            time.sleep(2)
            print(text)
            pyperclip.copy(text)
    except Exception as e:
        # print(e)
        pass

print("start")
while True:
    if keyboard.is_pressed('`'):
        work()
