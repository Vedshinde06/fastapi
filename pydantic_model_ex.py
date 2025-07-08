from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):
    
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str] #To validate that every value in the list is a string
    contact_details: Dict[str, str]
    
def insert_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print('inserted')
    
    
def update_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print('updated')    
    
patient_info = {'name': 'Vedant', 'age': 'thirty', 'weight': '59', 'married': 'True', 'allergies': ['dust', 'red chilli'], 'contact_details': {'email': 'xyz@kmail.com', 'Mob': '900689940'}}
patient1 = Patient(**patient_info)
    
insert_patient_data(patient1)
    
print("hello world")