import os
import cv2
import numpy as np

IMG_SIZE = 64

def load_data(dataset_path="cell_images/"):
    images, labels = [], []
    for label in ["Parasitized", "Uninfected"]:
        folder = os.path.join(dataset_path, label)
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            img = cv2.imread(file_path)
            
            if img is None:
                print("Warning: Could not read", file_path)
                continue  # skip this file
            
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            images.append(img)
            labels.append(1 if label=="Parasitized" else 0)
            
    X = np.array(images)/255.0
    y = np.array(labels)
    return X, y

# Test
if __name__ == "__main__":
    X, y = load_data()
    print("Data loaded:", X.shape, y.shape)