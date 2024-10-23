from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Path to the model
MODEL_PATH = 'plant_vs_non_plant_model.h5'

# Load the model
model = tf.keras.models.load_model(MODEL_PATH)

# Folder to store uploaded images
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Image size for VGG16 input
img_size = (224, 224)

# Function to predict if an image is plant or non-plant
def predict_image(img_path, model):
    # Load the image and preprocess it
    img = image.load_img(img_path, target_size=img_size)
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Make prediction
    prediction = model.predict(img_array)
    
    # Interpret prediction
    if prediction > 0.5:
        return f"Plant (Confidence: {prediction[0][0]*100:.2f}%)"
    else:
        return f"Not-Plant (Confidence: {(1-prediction[0][0])*100:.2f}%)"

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling the image upload and prediction
@app.route('/predict', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Predict the image class
        prediction = predict_image(file_path, model)
        return render_template('index.html', prediction=prediction, img_path=file_path)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
