import cv2
import numpy as np

def crop_aadhaar(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Blur to remove noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection
    edged = cv2.Canny(blur, 75, 200)
     
    # Find contours
    contours, _ = cv2.findContours(
        edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    if not contours:
        return image  # fallback

    # Sort contours by area (largest first)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        # Aadhaar card approx area filter
        if area < 50000:
            continue

        x, y, w, h = cv2.boundingRect(cnt)

        aspect_ratio = w / float(h)

        # Aadhaar card aspect ratio ~ 1.5–1.7
        if 1.3 < aspect_ratio < 1.9:
            return image[y:y+h, x:x+w]

    return image  # fallback if no good contour found
