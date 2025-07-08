from fastapi import FastAPI
import json

app = FastAPI()

# Function for loading data from json file
def load_data():
    with open ('patients.json', 'r') as f:
        data=json.load(f)
    return data    

@app.get("/")
def hello():
    return {'message':'Patient Management System API'}

@app.get("/about")
def About():
    return{'message':'This is an API for patient management system'}

# Endpoint for getting patient data(view)
@app.get("/view")
def View():
     data = load_data()
     
     return data
 
@app.get("/patient/{patient_id}")
def view_patient(patient_id : str):
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    return {'error':'Patient not found'}