from pydantic import BaseModel, Field, AnyUrl, EmailStr, model_validator, field_validator
from typing import List, Dict, Annotated, Optional

class Patient(BaseModel):

    name : str
    email : EmailStr
    age : int
    weight : float
    married : bool
    allergies : List[str]
    contact_detail : Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_detail:
            raise ValueError('Patient older than 60 must have an emergency contact')
        else:
            return model


def update_patient_detail(patient : Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_detail)

patient_info = {'name' : 'navneet', 'email' : 'abc@hdfc.com', 'age' : 65, 'weight' : 86.6, 'married' : True,  'allergies' : ['pollen', 'dust'],'contact_detail' : {'phone' : '9876543210', 'emergency' : '1234567890'}}

patient1 = Patient(**patient_info)
update_patient_detail(patient1)