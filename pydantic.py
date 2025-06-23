from pydantic import Basemodel

class Patient(Basemodel):
    
    name: str
    age: int


def insert_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print('inserted')
    
    
    patient_info = {'name': 'Vedant', 'age': '20'}
    
    patient1 = Patient(**patient_info)
    
    