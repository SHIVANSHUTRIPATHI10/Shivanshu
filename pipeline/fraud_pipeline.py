import sys
import os

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from ocr.simple_ocr import read_text
from rules.aadhaar_rules import run_rules


def run_fraud_pipeline(image_path):
    text = read_text(image_path)
    result = run_rules(text)
    return result


if __name__ == "__main__":
    image = "dataset/processed/real/99.jpg"
    output = run_fraud_pipeline(image)
    print(output)
