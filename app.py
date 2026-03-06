from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
import cv2
import numpy as np
import os

app = Flask(__name__)
# Enable CORS so your HTML file can communicate with this Python server
CORS(app)

# Configuration
MODEL_PATH = "malaria_model.h5"
IMG_SIZE = 64

# Safety check: Ensure the model exists before starting the server
if os.path.exists(MODEL_PATH):
    try:
        model = load_model(MODEL_PATH)
        print("Successfully loaded Malaria Detection Model.")
    except Exception as e:
        print(f"Error loading model file: {e}")
else:
    print(f"CRITICAL ERROR: {MODEL_PATH} not found in the current directory.")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # 1. Check if a file was sent in the request
        if "file" not in request.files:
            return jsonify({"error": "No file part in the request"}), 400

        file = request.files["file"]
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        

        # 2. Convert the uploaded file to an OpenCV image
        file_bytes = np.frombuffer(file.read(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        if img is None:
            return jsonify({"error": "Uploaded file is not a valid image"}), 400
        

        # 3. Preprocessing: Match the training input (64x64, normalized)
        img_resized = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        img_normalized = img_resized / 255.0
        img_final = np.expand_dims(img_normalized, axis=0)
        

        # 4. Run Model Prediction
        prediction_raw = model.predict(img_final)
        score = prediction_raw[0][0]


        # 5. Determine Label and Confidence
        # In binary classification, > 0.5 usually means Parasitized
        is_parasitized = score > 0.5
        label = "Parasitized" if is_parasitized else "Uninfected"
        
        # We calculate confidence as how sure the AI is of its CHOSEN label
        confidence = float(score if is_parasitized else 1.0 - score)


        # 6. Return professional JSON response
        return jsonify({
            "prediction": label,
            "confidence": round(confidence, 4),
            "stage_analyzed": "Erythrocytic (Blood) Stage",
            "status": "success"
        })

    except Exception as e:
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500

if __name__ == "__main__":
    # host 0.0.0.0 allows access from other devices on your local network
    app.run(host="0.0.0.0", port=5000, debug=False)