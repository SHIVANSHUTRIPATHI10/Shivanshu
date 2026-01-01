import os
from flask import Flask, render_template, request, jsonify
from pipeline.fraud_pipeline import run_fraud_pipeline

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/verify", methods=["POST"])
def verify():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty file name"})

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    result = run_fraud_pipeline(file_path)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
