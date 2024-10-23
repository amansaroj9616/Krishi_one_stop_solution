let stateCityObj = {
    "Andhra Pradesh": ["Vijayawada", "Guntur", "Visakhapatnam"],
    "Arunachal Pradesh": ["Ziro", "Itanagar", "Tawang"],
    "Assam": ["Guwahati", "Silchar", "Dibrugarh"],
    "Bihar": ["Bhagalpur", "Patna", "Gaya"],
    "Chhattisgarh": ["Raipur", "Durg", "Bilaspur"],
    "Delhi": ["Dwarka", "Karol Bagh", "New Delhi"],
    "Goa": ["Margao", "Panaji", "Vasco da Gama"],
    "Gujarat": ["Ahmedabad", "Surat", "Vadodara"],
    "Haryana": ["Panipat", "Faridabad", "Gurgaon"],
    "Himachal Pradesh": ["Manali", "Shimla", "Dharamshala"],
    "Jammu and Kashmir": ["Srinagar", "Jammu", "Anantnag"],
    "Jharkhand": ["Dhanbad", "Jamshedpur", "Ranchi"],
    "Karnataka": ["Mysuru", "Bengaluru", "Hubli"],
    "Kerala": ["Kozhikode", "Kochi", "Thiruvananthapuram"],
    "Ladakh": ["Nubra Valley", "Leh", "Kargil"],
    "Madhya Pradesh": ["Gwalior", "Bhopal", "Indore"],
    "Maharashtra": ["Mumbai", "Nagpur", "Pune"],
    "Manipur": ["Thoubal", "Imphal", "Bishnupur"],
    "Meghalaya": ["Tura", "Shillong", "Nongstoin"],
    "Mizoram": ["Serchhip", "Lunglei", "Aizawl"],
    "Nagaland": ["Dimapur", "Kohima", "Mokokchung"],
    "Odisha": ["Cuttack", "Bhubaneswar", "Rourkela"],
    "Puducherry": ["Karaikal", "Puducherry", "Yanam"],
    "Punjab": ["Jalandhar", "Ludhiana", "Amritsar"],
    "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur"],
    "Sikkim": ["Pelling", "Namchi", "Gangtok"],
    "Tamil Nadu": ["Coimbatore", "Madurai", "Chennai"],
    "Telangana": ["Hyderabad", "Nizamabad", "Warangal"],
    "Tripura": ["Udaipur", "Agartala", "Dharmanagar"],
    "Uttar Pradesh": ["Agra", "Kanpur", "Lucknow"],
    "Uttarakhand": ["Dehradun", "Nainital", "Haridwar"],
    "West Bengal": ["Kolkata", "Howrah", "Durgapur"]
};


let cityContainer=null;
let stateContainer=null;
document.addEventListener('DOMContentLoaded',function(){
    stateContainer=document.getElementById("State");
    cityContainer=document.getElementById('City');
    stateContainer.addEventListener('change', onSelectHandler);
    renderState(stateCityObj);
});

function onSelectHandler(event){
    let state=event.target.value;
    let cityArr=stateCityObj[state];
    renderAllOption(cityContainer, cityArr, "City");

}

function renderAllOption(parent, arr, name){
    parent.textContent="";

    let optionEl=document.createElement('option');
    optionEl.textContent="Select "+name;
    optionEl.value="";
    optionEl.disabled=true;
    optionEl.selected=true;
    parent.appendChild(optionEl);

    for(let optionVal of arr){
        renderOption(parent, optionVal);
    }
}

function renderOption(parent, value){
    let optionEl=document.createElement('option');
    optionEl.textContent=value;
    optionEl.value=value;
    parent.appendChild(optionEl);
}

function renderState(stateObj){
    let arr=[];
    for(let state in stateObj){
        arr.push(state);
    }
    renderAllOption(stateContainer,arr, "State");
}
