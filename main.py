from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data
    

@app.get("/")
def hello():
    return {"message": "Patient management system API"}

@app.get("/about")
def about():
    return {
        "message": "A fully functional API to manage your patient records"
    }


@app.get("/view")
def view():
    data = load_data()

    return data


@app.get("/patient/{patient_id}")
def view_patient(patient_id : str = Path(..., description='ID of the patient of the DB', example='P001')):
    #load all the data
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')

@app.get("/sort")
def sort_patient(sort_by : str = Query(..., description="Sort on the basis of Height, weight or BMI"), order : str = Query('asc', description="Sort by ascending or decending order")):

    valid_fields= ['height', 'weight', 'bmi']   

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select from asending or descnding')
    
    data = load_data()

    sort_order = True if sorted=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data