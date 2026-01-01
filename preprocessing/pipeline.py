import cv2
import os
import numpy as np   # ✅ REQUIRED
from preprocessing.deskew import deskew
from preprocessing.crop_aadhaar import crop_aadhaar
# from preprocessing.deskew import deskew


def preprocess_image(image_path, output_path):
    print("Using LOCAL pipeline.py")

    img = cv2.imread(image_path)

    if img is None:
        print(f" Cannot read image: {image_path}")
        return

    # 1️⃣ Resize
    img = cv2.resize(img, (1024, 1024))

    # 2️⃣ Denoise
    img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

    # 3️⃣ Sharpen (FIXED)
    kernel = np.array([
        [0, -1,  0],
        [-1, 5, -1],
        [0, -1,  0]
    ], dtype=np.float32)

    img = cv2.filter2D(img, -1, kernel)

    img = crop_aadhaar(img)

    # Ensure output folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    cv2.imwrite(output_path, img)
    print(f"✅ Processed: {os.path.basename(image_path)}")
    # img = deskew(img)
