from fastapi import FastAPI
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
def view_patient(patient_id : str):
    #load all the data
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    return {'error': 'patient is not found'}