from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List
from typing import Dict
from typing import Optional
from typing import Annotated

class Patient(BaseModel):

    name : Annotated[str, Field(max_length=50, title='Name of the patient', description='enter name less than 50 characters', examples=['Shantanu', 'Tushar'])]
    age : int = Field(gt=0, lt=120)
    linkedin_url : AnyUrl
    email : EmailStr
    weight : Annotated[float, Field(gt=0, strict= True)]
    married : Annotated[bool, Field(default=False, description='is the person married or not?')]
    allergies : Annotated[Optional[List[str]], Field(default = None, max_length=5)]  
    contact_details : Dict[str , str]

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted into database")


def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print("updated")


patient_info = {'name': 'Shantanu', 'age': '20', 'linkedin_url' : 'http://linkedin.com/1234', 'email': 'Shant@gmail.com', 'weight' : 49.2, 'married' : False, 'allergies' : ['pollen', 'dust'], 'contact_details':{'phone' : '123456'}}

patient1 = Patient(**patient_info)


insert_patient_data(patient1)
update_patient_data(patient1)
