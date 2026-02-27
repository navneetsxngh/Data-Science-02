from pydantic import BaseModel, Field, AnyUrl, EmailStr, field_validator
from typing import List, Dict, Annotated, Optional

class Patient(BaseModel):

    name : str
    email : EmailStr
    age : int
    weight : float
    married : bool
    allergies : List[str]
    contact_detail : Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']

        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a Valid Domain')
        else:
            return value
    
    @field_validator('name')
    @classmethod
    def name_validator(cls, value):
        return value.upper()
    
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')

def update_patient_detail(patient : Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_detail)

patient_info = {'name' : 'navneet', 'email' : 'abc@hdfc.com', 'age' : '30', 'weight' : 86.6, 'married' : True,  'allergies' : ['pollen', 'dust'],'contact_detail' : {'phone' : '9876543210'}}

patient1 = Patient(**patient_info)
update_patient_detail(patient1)