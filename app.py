# app.py
from tensorflow.keras.models import load_model
import cv2
import numpy as np

# Load the trained model
model = load_model("malaria_model.h5")
IMG_SIZE = 64

def predict_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)
    if pred[0][0] > 0.5:
        return "Parasitized"
    else:
        return "Uninfected"

# Test
if __name__ == "__main__":
    image_path = input("Enter path of cell image: ")
    result = predict_image(image_path)
    print("Prediction:", result)