import sys
import os
sys.path.append(os.getcwd())

from ocr.simple_ocr import read_text
from rules.aadhaar_rules import run_rules

text = read_text("dataset/processed/real/99.jpg")

result = run_rules(text)

print("FINAL RESULT:")
print(result)
