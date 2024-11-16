import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "Vehicle_Age": 7,
    "Mileage": 80000,
    "Engine_Size": 2.2,
    "Owner_Type": 1,
    "Vehicle_Model": 0,
    "Maintenance_History": 0,
    "Reported_Issues": 0,
    "Fuel_Type": 0,
    "Transmission_Type": 0,
    "Odometer_Reading": 0,
    "Last_Service_Date": 0,
    "Warranty_Expiry_Date": 0,
    "Insurance_Premium": 0,
    "Service_History": 0,
    "Accident_History": 0,
    "Fuel_Efficiency": 0,
    "Tire_Condition": 0,
    "Brake_Condition": 0,
    "Battery_Status": 0
}

response = requests.post(url, json=data)
print(response.json())