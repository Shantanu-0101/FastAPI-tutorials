from pydantic import BaseModel, EmailStr, AnyUrl, model_validator
from typing import List
from typing import Dict


class Patient(BaseModel):

    name : str
    age : int
    linkedin_url : AnyUrl
    email : EmailStr
    weight : float
    married : bool
    allergies : List[str]
    contact_details : Dict[str , str]

    @model_validator(mode='after')
    def emergency_contact(cls, model):
          if model.age > 60 and 'emergency' not in model.contact_details:
                raise ValueError('Patient older than 60 must have emergency contact')
          return model


def update_patient_data(patient : Patient):
        print(patient.name)
        print(patient.age)
        print(patient.allergies)
        print(patient.married)
        print("updated")


patient_info = {'name': 'Shantanu', 'age': 66, 'linkedin_url' : 'http://linkedin.com/1234', 'email': 'Shant@hdfc.com', 'weight' : 49.2, 'married' : False, 'allergies' : ['pollen', 'dust'], 'contact_details':{'phone' : '123456', 'emergency': '38292'}}

patient1 = Patient(**patient_info) #validation -> type coersion


update_patient_data(patient1)
