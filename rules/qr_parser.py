import re

def parse_qr_data(qr_text):
    if not qr_text:
        return None

    aadhaar = re.search(r"\d{12}", qr_text)
    dob = re.search(r"\d{2}/\d{2}/\d{4}", qr_text)

    return {
        "aadhaar": aadhaar.group(0) if aadhaar else None,
        "dob": dob.group(0) if dob else None
    }
