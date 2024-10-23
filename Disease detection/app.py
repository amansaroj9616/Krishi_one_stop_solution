from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import json
import os
import io

app = Flask(__name__)
CORS(app)
# Load your trained model
model = load_model('plant_disease_cnn_model.h5')

# Create a mapping from class indices to disease names
class_names = {
    0: 'Apple Scab',
    1: 'Apple Black Rot',
    2: 'Apple Cedar Apple Rust',
    3: 'Apple Healthy',
    4: 'Bacterial Leaf Blight in Rice Leaf',
    5: 'Blight in Corn Leaf',
    6: 'Blueberry Healthy',
    7: 'Brown Spot in Rice Leaf',
    8: 'Cercospora Leaf Spot',
    9: 'Cherry Powdery Mildew',
    10: 'Cherry Healthy',
    11: 'Common Rust in Corn Leaf',
    12: 'Corn Healthy',
    13: 'Garlic',
    14: 'Grape Black Rot',
    15: 'Grape Esca (Black Measles)',
    16: 'Grape Leaf Blight (Isariopsis Leaf Spot)',
    17: 'Grape Healthy',
    18: 'Gray Leaf Spot in Corn Leaf',
    19: 'Leaf Smut in Rice Leaf',
    20: 'Nitrogen Deficiency in Plant',
    21: 'Orange Huanglongbing (Citrus Greening)',
    22: 'Peach Healthy',
    23: 'Pepper Bell Bacterial Spot',
    24: 'Pepper Bell Healthy',
    25: 'Potato Early Blight',
    26: 'Potato Late Blight',
    27: 'Potato Healthy',
    28: 'Raspberry Healthy',
    29: 'Sogatella in Rice',
    30: 'Soybean Healthy',
    31: 'Strawberry Leaf Scorch',
    32: 'Strawberry Healthy',
    33: 'Tomato Bacterial Spot',
    34: 'Tomato Early Blight',
    35: 'Tomato Late Blight',
    36: 'Tomato Leaf Mold',
    37: 'Tomato Septoria Leaf Spot',
    38: 'Tomato Spider Mites (Two-Spotted Spider Mite)',
    39: 'Tomato Target Spot',
    40: 'Tomato Mosaic Virus',
    41: 'Tomato Healthy',
    42: 'Waterlogging in Plant',
    43: 'Algal Leaf in Tea',
    44: 'Anthracnose in Tea',
    45: 'Bird Eye Spot in Tea',
    46: 'Brown Blight in Tea',
    47: 'Cabbage Looper',
    48: 'Corn Crop',
    49: 'Ginger',
    50: 'Healthy Tea Leaf',
    51: 'Lemon Canker',
    52: 'Onion',
    53: 'Potassium Deficiency in Plant',
    54: 'Potato Crop',
    55: 'Potato Hollow Heart',
    56: 'Red Leaf Spot in Tea',
    57: 'Tomato Canker'
}


def preprocess_image(img):
    img = img.resize((128, 128))  # Adjust according to your model input size
    img = img.convert('RGB')
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

# Home route that displays the web form
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle prediction and return results
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if the post request has the file part
        if 'image' not in request.files:
            return render_template('index.html', error="No image uploaded!")

        img_file = request.files['image']

        # If no file is selected
        if img_file.filename == '':
            return render_template('index.html', error="No image selected!")

        # Convert image file to PIL Image
        img = Image.open(io.BytesIO(img_file.read()))
        img = preprocess_image(img)

        # Predict using the model
        predictions = model.predict(img)
        class_index = np.argmax(predictions, axis=1)[0]

        # Map the class index to the disease name
        disease_name = class_names.get(class_index, "Unknown Disease")

        # return render_template('result.html', prediction=disease_name)
        
        # Load the external cure.json file
        json_path = os.path.join(os.path.dirname(__file__), 'cure.json')
        with open(json_path, 'r',encoding='utf-8') as file:
            cure_data = json.load(file)
        
        cure_returned_data=cure_data[disease_name.lower()]
    
        return jsonify({'prediction': disease_name,'cure': cure_returned_data}), 200

    except Exception as e:
        print(e)
        return jsonify({'error':"Something went wrong!"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

