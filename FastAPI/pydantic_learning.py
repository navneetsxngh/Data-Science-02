## Why we need pydantic
# Pydantic validates, parses, and structures your data automatically.
# Without it, you manually check everything.
# With it, FastAPI becomes powerful.

## To remove type validation and data validation


## Data Validation
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# Annotated = To add meta data

class Patient(BaseModel):
    name : Annotated[str, Field(max_length=50, title='Name of the Patient', description='Give name of the patient', examples= ['Navneet', 'Devendra'])]  ## max characters = 50
    email : EmailStr
    linkedin_url : AnyUrl
    age : int = Field(gt=0, lt=120)  #gt = greater than, lt = less than
    weight : Annotated[float, Field(gt=0, strict=True)]
    marital_status : Annotated[bool, Field(default=None, description= 'Is the patient Married or not')]   ## Optional Field, by default is is none
    allergies : Annotated[Optional[List[str]], Field(default=None, max_length=5)] ## A list with all the values are string
    contact_details : Dict[str, str]  ## A Dictionary with key and values both are str

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.marital_status)
    print(patient.allergies)
    print("Inserted")

patient_info = {'name' : 'Navneet', 'email' : 'abc@gmail.com', 'linkedin_url' : 'https://www.linkedin.com/feed/1235', 'age' : 30, 'weight' : 86.6, 'marital_status' : True,  'allergies' : ['pollen', 'dust'],'contact_details' : {'phone' : '9876543210'}}
# patient_info = {'name' : 'Navneet', 'age' : 30, 'weight' : '86'}
patient1 = Patient(**patient_info)

insert_patient_data(patient1)