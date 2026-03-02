from tensorflow.keras.models import load_model
import cv2
import numpy as np

model = load_model("malaria_model.h5")
IMG_SIZE = 64

def predict_image(image_path):
    img = cv2.imread(image_path)
    
    if img is None:
        print("Image not found. Check the path.")
        return
    
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    if prediction[0][0] > 0.5:
        print("Prediction: Parasitized")
    else:
        print("Prediction: Uninfected")

if __name__ == "__main__":
    path = input("Enter full image path: ")
    predict_image(path)