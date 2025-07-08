from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    
    name: Annotated[str, Field(max_length=96, title='Name of the Patient', description='Here we can give the description for our datatype', examples=['Raj'])]
    email: EmailStr
    Linkedin_URL: AnyUrl
    age: int
    weight: Annotated[float, Field(gt=0, strict=True)] # Age should be greater than zero
    height: float
    married: bool = False
    allergies: Optional[List[str]] = None #To validate that every value in the list is a string
    contact_details: Dict[str, str]
    
    # For Data validation
    @field_validator('email')
    @classmethod
    def email_validator(cla, value):
        
        Valid_domains = ['gmail.com', 'yahoo.com']

        domain_name= value.split('@')[-1]
        
        if domain_name not in Valid_domains:
            raise ValueError('Not a valid domain, Only gmail and yahoo accepted')
        
        return value
    
    
    # For data transformation
    @field_validator('name')
    @classmethod
    def Name_validator(cls, value):
        return value.upper()
    
    #For using other values
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have emergency contact')
        return model
    
    @computed_field
    @property
    def bmi(self) -> float:

        bmi=round(self.weight / self.height**2, 2)
        return bmi
    
        
def insert_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print('BMI', patient.bmi)
    print('inserted')
    
    
def update_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print('updated')    
    
patient_info = {'name': 'Vedant', 'email': 'vedu@gmail.com', 'Linkedin_URL': 'https://xyz.com', 'age': '62', 'weight': 59, 'height': 0.6, 'married': 'True', 'allergies': ['dust', 'red chilli'], 'contact_details': {'email': 'xyz@kmail.com', 'Mob': '900689940', 'emergency': '957684839'}}

patient1 = Patient(**patient_info)
    
insert_patient_data(patient1)
    
