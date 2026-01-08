🛡️ AadhaarSentinel: Intelligent Identity Fraud Detection System

AadhaarSentinel is an AI-powered Aadhaar verification and fraud detection system designed to identify fake, tampered, or suspicious Aadhaar documents.
The platform combines Computer Vision, OCR, and Explainable Rule-Based Intelligence to deliver a secure, transparent, and real-time identity verification workflow through a modern web application.
🚀 Key Features
🔍 Multi-Stage Verification Workflow

1️⃣ Document Analysis

Preprocesses Aadhaar images using OpenCV (resize, denoise, sharpen, deskew)
Ensures only Aadhaar-like documents proceed for further analysis
Filters noisy, rotated, and low-quality images to improve OCR accuracy

2️⃣ Identity Data Extraction (OCR)

Extracts Aadhaar details using Tesseract OCR
Automatically detects and parses:
Aadhaar / VID number
Date of Birth (DOB)
Gender

Handles real-world image conditions such as blur, lighting variation, and resolution issues

3️⃣ Rule-Based Fraud Validation
Applies explainable, auditable validation rules:
Aadhaar / VID format verification
DOB format consistency checks
Gender presence validation
Missing or inconsistent field detection
Produces a clear verification decision:

✅ REAL

❌ SUSPICIOUS
🛠️ Tech Stack

Backend

Python 3.x
Flask

Computer Vision & OCR

OpenCV
Tesseract OCR
Fraud Detection
Rule-Based Explainable Validation Engine

Frontend

HTML5
CSS3
JavaScript (Fetch API)
