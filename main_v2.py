from fastapi import FastAPI, HTTPException, Path, Query
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
def view_patient(
    patient_id: str = Path(..., description="Enter patient ID", examples={"example1": {"value": "P001"}})
):
    data = load_data()  # Make sure load_data() returns a dictionary
    
    if patient_id in data:
        return data[patient_id]
    
    # Correct way to return an error
    raise HTTPException(status_code=404, detail="Patient not found")
