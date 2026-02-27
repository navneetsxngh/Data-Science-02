from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import json

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)

app = FastAPI()

class Patient(BaseModel):

    id : Annotated[str, Field(..., description='ID of the Patient', examples=['P001'])]
    name : Annotated[str, Field(..., description='Name of the Patient')]
    city : Annotated[str, Field(..., description='City where the patient resides')]
    age : Annotated[int, Field(gt=0, lt=120, description='Age of the Patient')]
    gender : Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the Patient')]
    height : Annotated[float, Field(..., gt=0, description='Height of the Patient in meters')]
    weight : Annotated[float, Field(..., gt=0, description='Weight of the patient in kgs')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'UnderWeight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'

@app.get("/")
def hello():
    return {"message" : "Patient Management System API"}

@app.get('/about')
def about():
    return {'message' : 'A fully Functional API to manage your patient records'}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description="ID of the Patient in the Database", example= "P001")):
    ## Load all the functions
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404, detail='Patient Not found')
    

@app.get('/sort')
def sort(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query(..., description='sort in asc or desc order')):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid Field, Select from {valid_fields}")
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid Order select between asc and desc')
    
    data = load_data()
    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x : x.get(sort_by, 0), reverse=sort_order)

    return sorted_data

@app.post('/create')
def create_patient(patient : Patient):
    ## load the existing Dataset
    data = load_data()

    ## Check if patient is already exist
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient Already Exist")
    
    # New Patient adds to the database
    data[patient.id] = patient.model_dump(exclude= ['id'])

    # save into the json file
    save_data(data)

    return JSONResponse(status_code=201, content= {'message' : 'Patient created Successfully'})
