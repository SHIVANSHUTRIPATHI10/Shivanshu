import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from preprocessing.pipeline import preprocess_image

input_dir = "dataset/aadhaar/real"
output_dir = "dataset/processed/real"

for img in os.listdir(input_dir):
    preprocess_image(
        os.path.join(input_dir, img),
        os.path.join(output_dir, img)
    )

print(" All images preprocessed successfully")
