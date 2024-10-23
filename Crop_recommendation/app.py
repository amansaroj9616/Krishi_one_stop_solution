from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('final_model.pkl', 'rb'))

# Create a dictionary to map city and state to numerical values (example)
city_mapping ={
    "Pelling": 71,
    "Mumbai": 59,
    "Nubra Valley": 67,
    "Srinagar": 81,
    "Jalandhar": 39,
    "Kolkata": 49,
    "Coimbatore": 13,
    "Dimapur": 20,
    "Madurai": 55,
    "Namchi": 63,
    "Mysuru": 60,
    "Gwalior": 30,
    "Bhopal": 8,
    "Panipat": 69,
    "Kozhikode": 50,
    "Tura": 86,
    "Agra": 1,
    "Jammu": 40,
    "Ahmedabad": 2,
    "Kochi": 47,
    "Margao": 57,
    "Udaipur": 87,
    "Kanpur": 43,
    "Raipur": 74,
    "Bhagalpur": 7,
    "Faridabad": 24,
    "Dhanbad": 16,
    "Vijayawada": 90,
    "Gangtok": 25,
    "Ziro": 94,
    "Patna": 70,
    "Shillong": 78,
    "Gurgaon": 28,
    "Lucknow": 52,
    "Ludhiana": 53,
    "Kohima": 48,
    "Panaji": 68,
    "Jaipur": 38,
    "Jodhpur": 42,
    "Thoubal": 85,
    "Agartala": 0,
    "Durg": 21,
    "Bengaluru": 6,
    "Indore": 36,
    "Itanagar": 37,
    "Dehradun": 15,
    "Anantnag": 5,
    "Chennai": 12,
    "Manali": 56,
    "Cuttack": 14,
    "Karaikal": 44,
    "Serchhip": 77,
    "Leh": 51,
    "Vasco da Gama": 89,
    "Bilaspur": 10,
    "Nainital": 62,
    "Dharmanagar": 18,
    "Puducherry": 72,
    "Lunglei": 54,
    "Guwahati": 29,
    "Silchar": 80,
    "Dwarka": 23,
    "Tawang": 83,
    "Mokokchung": 58,
    "Surat": 82,
    "Gaya": 26,
    "Guntur": 27,
    "Shimla": 79,
    "Hyderabad": 34,
    "Nongstoin": 66,
    "Aizawl": 3,
    "Yanam": 93,
    "Amritsar": 4,
    "Imphal": 35,
    "Dibrugarh": 15,
    "Karol Bagh": 46,
    "Haridwar": 31,
    "Nizamabad": 65,
    "Jamshedpur": 41,
    "Howrah": 32,
    "New Delhi": 64,
    "Bhubaneswar": 9,
    "Nagpur": 61,
    "Durgapur": 22,
    "Dharamshala": 17,
    "Vadodara": 88,
    "Visakhapatnam": 91,
    "Rourkela": 76,
    "Pune": 73,
    "Thiruvananthapuram": 84,
    "Bishnupur": 11,
    "Kargil": 45,
    "Ranchi": 75,
    "Hubli": 33,
    "Warangal": 92
}
 # Add more mappings as per your dataset
state_mapping ={
    "Andhra Pradesh": 0,
    "Arunachal Pradesh": 1,
    "Assam": 2,
    "Bihar": 3,
    "Chhattisgarh": 4,
    "Delhi": 5,
    "Goa": 6,
    "Gujarat": 7,
    "Haryana": 8,
    "Himachal Pradesh": 9,
    "Jammu and Kashmir": 10,
    "Jharkhand": 11,
    "Karnataka": 12,
    "Kerala": 13,
    "Ladakh": 14,
    "Madhya Pradesh": 15,
    "Maharashtra": 16,
    "Manipur": 17,





    
    "Meghalaya": 18,
    "Mizoram": 19,
    "Nagaland": 20,
    "Odisha": 21,
    "Puducherry": 22,
    "Punjab": 23,
    "Rajasthan": 24,
    "Sikkim": 25,
    "Tamil Nadu": 26,
    "Telangana": 27,
    "Tripura": 28,
    "Uttar Pradesh": 29,
    "Uttarakhand": 30,
    "West Bengal": 31
}
 # Add more mappings as per your dataset

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Extract form data
        nitrogen = float(request.form['Nitrogen'])
        phosphorus = float(request.form['Phosphorus'])
        potassium = float(request.form['Potassium'])
        temperature = float(request.form['Temperature'])
        humidity = float(request.form['Humidity'])
        ph = float(request.form['pH'])
        rainfall = float(request.form['Rainfall'])
        
        # Get City and State from the form and convert to numeric
        city = request.form['City']
        city=city_mapping[city.capitalize()]
        
        state = request.form['State']
        state=state_mapping[state.capitalize()]
        


        # Create input array for the model with all 9 features
        input_features = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall, state, city]])

        # Predict the crop
        prediction = model.predict(input_features)
        crop = prediction[0]  # Get the predicted crop
        

        # Render the result in the same template
        return render_template('index.html', result=crop)

if __name__ == "__main__":
    app.run(debug=True)
