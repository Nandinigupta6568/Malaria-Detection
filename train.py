# train.py

print("🚀 train.py is running")  # debug

from data_preprocessing import load_data
from model import create_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split

print("✅ Imports done")  # debug

def main():
    print("🏁 main() started")  # debug

    # Load dataset
    X, y = load_data()
    print("Data loaded:", X.shape, y.shape)

    # Split dataset
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    print("Data split done:", X_train.shape, X_val.shape)

    # Data augmentation
    train_datagen = ImageDataGenerator(
        rotation_range=15,
        width_shift_range=0.1,
        height_shift_range=0.1,
        horizontal_flip=True
    )
    val_datagen = ImageDataGenerator()

    train_gen = train_datagen.flow(X_train, y_train, batch_size=32)
    val_gen = val_datagen.flow(X_val, y_val, batch_size=32)

    # Create model
    model = create_model()
    print("Model created")  # debug

    # Train model
    history = model.fit(train_gen, validation_data=val_gen, epochs=20, verbose=1)
    print("Training finished")

    # Save model
    model.save("malaria_model.h5")
    print("Model saved!")

if __name__ == "__main__":
    main()