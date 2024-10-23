import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Image size for VGG16 input
img_size = (224, 224)

# Load the trained model
model = tf.keras.models.load_model('plant_vs_non_plant_model.h5')

# Function to predict if an image is plant or non-plant
def predict_image(img_path, model):
    # Check if the image file exists
    if not os.path.exists(img_path):
        print(f"Error: File {img_path} not found.")
        return

    # Load the image and preprocess it
    img = image.load_img(img_path, target_size=img_size)  # Load image with target size
    img_array = image.img_to_array(img) / 255.0           # Convert to array and normalize
    img_array = np.expand_dims(img_array, axis=0)         # Expand dimensions for model input
    
    # Make prediction
    prediction = model.predict(img_array)
    
    # Interpret prediction
    if prediction > 0.5:
        print(f"Predicted: Plant (Confidence: {prediction[0][0]*100:.2f}%)")
    else:
        print(f"Predicted: Not-Plant (Confidence: {(1-prediction[0][0])*100:.2f}%)")

# Example usage:
# Replace 'test_image.jpg' with the path of the image you want to predict
predict_image('pexels-orlovamaria-4915614.jpg', model)
