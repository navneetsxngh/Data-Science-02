# def insert_patient_data(name: str, age: int):
#     if type(name) == str and type(age) == int:
#         print(name)
#         print(age)
#         print("Data Inserted to DB")
#     else:
#         raise TypeError("Incorrect data Type")

# def update_patient_data(name: str, age: int):
#     if type(name) == str and type(age) == int:
#         print(name)
#         print(age)
#         print("Data Updated to DB")
#     else:
#         raise TypeError("Incorrect data Type")

# insert_patient_data("Navneet Singh", 25)

## Why we need pydantic
# Pydantic validates, parses, and structures your data automatically.
# Without it, you manually check everything.
# With it, FastAPI becomes powerful.

## To remove type validation and data validation


## Data Validation
from pydantic import BaseModel

class Patient(BaseModel):
    name : str
    age : int
    weight : float

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted")

patient_info = {'name' : 'Navneet', 'age' : 30, 'weight' : 86}
# patient_info = {'name' : 'Navneet', 'age' : 30, 'weight' : '86'}
patient1 = Patient(**patient_info)

insert_patient_data(patient1)