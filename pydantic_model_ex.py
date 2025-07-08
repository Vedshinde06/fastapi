from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional

class Patient(BaseModel):
    
    name: str
    email: EmailStr
    Linkedin_URL: AnyUrl
    age: int
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None #To validate that every value in the list is a string
    contact_details: Dict[str, str]
    
def insert_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print('inserted')
    
    
def update_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print('updated')    
    
patient_info = {'name': 'Vedant', 'email': 'vedu@email.com', 'Linkedin_URL': 'https://xyz.com', 'age': '30', 'weight': '59', 'married': 'True', 'allergies': ['dust', 'red chilli'], 'contact_details': {'email': 'xyz@kmail.com', 'Mob': '900689940'}}

patient1 = Patient(**patient_info)
    
insert_patient_data(patient1)
    
print("hello world")