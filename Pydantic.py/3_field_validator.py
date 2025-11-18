from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
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


    @field_validator('email')
    @classmethod
    def email_validator(cls,value):

        valid_domains = ['hdfc.com', 'icici.com']
        #abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Invalid Domain name')
        
        return value
    

    @field_validator('name')
    @classmethod
    def name_validator(cls, value):
        return value.upper()
    

    @field_validator('age', mode='before')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in bwtween 0 and 100')


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


patient_info = {'name': 'Shantanu', 'age': 20, 'linkedin_url' : 'http://linkedin.com/1234', 'email': 'Shant@hdfc.com', 'weight' : 49.2, 'married' : False, 'allergies' : ['pollen', 'dust'], 'contact_details':{'phone' : '123456'}}

patient1 = Patient(**patient_info) #validation -> type coersion


insert_patient_data(patient1)
update_patient_data(patient1)
