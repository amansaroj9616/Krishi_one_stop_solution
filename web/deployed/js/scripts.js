let isHindi = false;

function toggleLanguage() {
    isHindi = !isHindi;
    const langToggleBtn = document.getElementById('nav_btns');
    const welcomeMessage = document.querySelector('.welcome-section h2');
    const welcomeDesc = document.querySelector('.welcome-section p');
    const assistanceBtn = document.getElementById('assistance-btn');

    if (isHindi) {
        langToggleBtn.textContent = 'हिंदी';
        welcomeMessage.textContent = 'कृषि में आपका स्वागत है!';
        welcomeDesc.textContent = 'बेहतर खेती, फसल अनुशंसा और बाजार अंतर्दृष्टि के लिए आपका प्रवेश द्वार।';
        assistanceBtn.textContent = 'सहायता शुरू करें';
    } else {
        langToggleBtn.textContent = 'English';
        welcomeMessage.textContent = 'Welcome to Krishi!';
        welcomeDesc.textContent = 'Your gateway to better farming practices, crop recommendations, and market insights.';
        assistanceBtn.textContent = 'Start Assistance';
    }
}

// Cache DOM elements to improve performance
const navToggleBtn = document.getElementById('nav_btns');
navToggleBtn.addEventListener('click', toggleLanguage);

navToggleBtn.addEventListener('click', function() {
    alert("AI-powered assistance will be available here soon!");
});

// ***************** Crop Recommendations ************************************************************
// Function to fetch location using HTML5 Geolocation API
function getLocation() {
    const locationStatus = document.getElementById('location-status');
    
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
      locationStatus.textContent = "Geolocation is not supported by this browser.";
    }
}
  
// Function to handle successful retrieval of location
function showPosition(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;

    document.getElementById('location-status').textContent = `Latitude: ${latitude}, Longitude: ${longitude}`;
    
    fetchWeatherData(latitude, longitude);
}
  
// Handle errors with Geolocation
function showError(error) {
    const locationStatus = document.getElementById('location-status');
    switch(error.code) {
      case error.PERMISSION_DENIED:
        locationStatus.textContent = "User denied the request for Geolocation.";
        break;
      case error.POSITION_UNAVAILABLE:
        locationStatus.textContent = "Location information is unavailable.";
        break;
      case error.TIMEOUT:
        locationStatus.textContent = "The request to get user location timed out.";
        break;
      case error.UNKNOWN_ERROR:
        locationStatus.textContent = "An unknown error occurred.";
        break;
    }
}
  
// Fetch weather data from the OpenWeatherMap API
async function fetchWeatherData(latitude, longitude) {
    const apiKey = 'fea401b17dd808bf8cf9fa49652bc98e';  // Replace with your OpenWeatherMap API key
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&units=metric&appid=${apiKey}`;
  
    try {
        const response = await fetch(apiUrl);
        if (!response.ok) throw new Error('Network response was not ok');
        const data = await response.json();
        displayWeatherAndCropRecommendation(data);
    } catch (error) {
        console.error('Error fetching weather data:', error);
        document.getElementById('weather-info').textContent = 'Failed to fetch weather data.';
    }
}

// Display weather and recommended crops
function displayWeatherAndCropRecommendation(weatherData) {
    const weatherElement = document.getElementById('weather-info');
    
    const temperature = weatherData.main.temp;
    const weatherDescription = weatherData.weather[0].description;
    const locationName = weatherData.name;
    
    let recommendedCrop = "";
    if (temperature > 30) {
      recommendedCrop = "Rice";
    } else if (temperature > 20 && temperature <= 30) {
      recommendedCrop = "Wheat";
    } else {
      recommendedCrop = "Barley";
    }
    
    weatherElement.innerHTML = `
      <h3>Weather in ${locationName}</h3>
      <p>Temperature: ${temperature}°C</p>
      <p>Condition: ${weatherDescription}</p>
      <h4>Recommended Crop: ${recommendedCrop}</h4>
      <p>Based on current weather conditions in your area, it's ideal to grow ${recommendedCrop}.</p>
    `;
}

// Call the function to start location detection and crop recommendation
getLocation();

// ********************** Crop Disease Detection ******************************************************

const imageUpload = document.getElementById('imageUpload');
const imagePreview = document.getElementById('imagePreview');
const diseaseResult = document.getElementById('disease-result');

// Preview the uploaded image
imageUpload.addEventListener('change', function () {
    const file = imageUpload.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            imagePreview.innerHTML = `<img src="${e.target.result}" alt="Crop Image" class="img-fluid" style="max-width: 100%; border-radius: 10px;" />`;
        };
        reader.readAsDataURL(file);
    } else {
        imagePreview.innerHTML = '';
    }
});

// Placeholder for disease detection (replace with AI/ML integration later)
document.getElementById('uploadForm').addEventListener('submit', function (e) {
    e.preventDefault();
    diseaseResult.innerHTML = 'Processing image... Disease detection coming soon!';
});

// **************************** Login/Sign-up page **************************************************

document.addEventListener('DOMContentLoaded', function () {
    const loginBtn = document.getElementById('login-btn');
    const signupBtn = document.getElementById('signup-btn');
    const loginForm = document.getElementById('login-form');
    const signupForm = document.getElementById('signup-form');

    loginBtn.addEventListener('click', function () {
        loginForm.classList.add('active');
        signupForm.classList.remove('active');
        loginBtn.classList.add('active');
        signupBtn.classList.remove('active');
    });

    signupBtn.addEventListener('click', function () {
        signupForm.classList.add('active');
        loginForm.classList.remove('active');
        signupBtn.classList.add('active');
        loginBtn.classList.remove('active');
    });
});
