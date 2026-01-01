import re
from datetime import datetime

def extract_fields(text):
    aadhaar = re.search(r"\b\d{4}\s\d{4}\s\d{4}\b", text)
    vid = re.search(r"\b\d{4}\s\d{4}\s\d{4}\s\d{4}\b", text)
    dob = re.search(r"\b\d{2}/\d{2}/\d{4}\b", text)
    gender = re.search(r"\b(MALE|FEMALE)\b", text, re.IGNORECASE)

    return {
        "aadhaar": aadhaar.group(0) if aadhaar else None,
        "vid": vid.group(0) if vid else None,
        "dob": dob.group(0) if dob else None,
        "gender": gender.group(0) if gender else None
    }


def validate_dob(dob):
    try:
        datetime.strptime(dob, "%d/%m/%Y")
        return True
    except:
        return False


def run_rules(ocr_text):
    fields = extract_fields(ocr_text)
    issues = []

    if not fields["aadhaar"] and not fields["vid"]:
        issues.append("Missing Aadhaar/VID number")

    if fields["dob"] and not validate_dob(fields["dob"]):
        issues.append("Invalid DOB format")

    if not fields["gender"]:
        issues.append("Gender missing")

    status = "REAL" if len(issues) == 0 else "SUSPICIOUS"

    return {
        "status": status,
        "fields": fields,
        "issues": issues
    }
def qr_match_check(ocr_fields, qr_fields):
    issues = []

    if qr_fields:
        if ocr_fields["aadhaar"] and qr_fields["aadhaar"]:
            if ocr_fields["aadhaar"].replace(" ", "") != qr_fields["aadhaar"]:
                issues.append("Aadhaar mismatch with QR")

        if ocr_fields["dob"] and qr_fields["dob"]:
            if ocr_fields["dob"] != qr_fields["dob"]:
                issues.append("DOB mismatch with QR")

    return issues
