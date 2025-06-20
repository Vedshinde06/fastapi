from fastapi import FastAPI, Path, HTTPException
import json

app = FastAPI()

def load_data():
    with open ('patients.json', 'r') as f:
        data = json.load(f)
        
    return data    

@app.get("/")
def hello():
    return {'message' : 'Patient Management System API'}

@app.get("/about")
def about():
    return { 'message':'A fully functional API to manage your patients records'}

@app.get("/view")
def veiw():
    data = load_data()
    
    return data

@app.get("/patient/{patient_id}")
def patient(patient_id: str = Path(..., description= 'ID of the patient in DB', example='P001')):
    # to load all patients
    data = load_data()
    
    if patient_id in data :
        return data[patient_id]
    
    raise HTTPException(status_code=404, details='Error not found')

