import sys
import os

# ✅ Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from ocr.simple_ocr import read_text

text = read_text("dataset/processed/real/99.jpg")

print("OCR OUTPUT:")
print(text)
