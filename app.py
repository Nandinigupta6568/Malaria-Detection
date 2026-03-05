from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
import cv2
import numpy as np

app = Flask(__name__)
CORS(app)

model = load_model("malaria_model.h5")
IMG_SIZE = 64

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    file_bytes = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if img is None:
        return jsonify({"error": "Invalid image"}), 400

    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)
    label = "Parasitized" if prediction[0][0] > 0.5 else "Uninfected"
    confidence = float(prediction[0][0])

    return jsonify({"prediction": label, "confidence": confidence})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)