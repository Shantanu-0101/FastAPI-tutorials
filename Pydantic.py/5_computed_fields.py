from pydantic import BaseModel, EmailStr,  computed_field
from typing import List
from typing import Dict


class Patient(BaseModel):

    name : str
    email : EmailStr
    age : int
    height : float
    weight : float
    married : bool
    allergies : List[str]
    contact_details : Dict[str , str]

    @computed_field
    @property
    def bmi(self) -> float:
          bmi = round(self.weight/(self.height**2),2)
          return bmi
          


def update_patient_data(patient : Patient):
        print(patient.name)
        print(patient.age)
        print(patient.allergies)
        print(patient.married)
        print(patient.bmi)
        print("updated")


patient_info = {'name': 'Shantanu', 'age': 66, 'email': 'Shant@hdfc.com','height':1.75, 'weight' : 100.2, 'married' : False, 'allergies' : ['pollen', 'dust'], 'contact_details':{'phone' : '123456', 'emergency': '38292'}}

patient1 = Patient(**patient_info) #validation -> type coersion


update_patient_data(patient1)
