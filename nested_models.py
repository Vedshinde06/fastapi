
#To organize hierarchy in data nested models are used

from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pincode: int
    
class Patient(BaseModel):
    
    name: str
    address: Address
    
    
address = {'city':'Satara', 'state':'maharashtra', 'pincode': 412801}

addr1 = Address(**address)

patient_info = {'name': 'Ramesh', 'address': addr1}

patient1_obj= Patient(**patient_info)

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.address.city)
    
insert_patient(patient1_obj)


temp = patient1_obj.model_dump_json()# here we can use include and exclude parameters for specific values
print(temp)                          # also exclude_unset can be used
print(type(temp))

temp = patient1_obj.model_dump()
print(temp)
print(type(temp))