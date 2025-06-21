from fastapi import FastAPI, Path, HTTPException, Query
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
def view():
    data = load_data()
    
    return data

@app.get("/patient/{patient_id}")
def patient(patient_id: str = Path(..., description= 'ID of the patient in DB', examples={"example1" : {"value":"P001"}})):
    
    # to load all patients
    data = load_data()
    
    if patient_id in data :
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')

@app.get("/sort")
def sort_patients(sort_by : str = Query(..., description='Sort on the basis of Height, Weight or BMI'), order: str = Query('asc', description = 'Sort in asc or decs order')):
    
    valid_fields = ['height', 'weight', 'bmi']
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code=404, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'decs']:
        raise HTTPException(status_code=404, detail='Invalid order select between asc or desc')
    
    data = load_data()
    
    sort_order= True if order =='decs' else False 
    
    sorted_data = sorted(data.values(), key= lambda x : x.get(sort_by, 0), reverse=sort_order)
    
    return sorted_data