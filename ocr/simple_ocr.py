import pytesseract
import cv2
import os
#  Python where tesseract is installed
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def read_text(image_path):
    img = cv2.imread(image_path)
    # print(img)
    if img is None:
        return ""

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # OCR
    text = pytesseract.image_to_string(gray, lang="eng")
    # print(text)
    return text
