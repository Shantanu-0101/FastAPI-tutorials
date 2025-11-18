from pydantic import BaseModel


class Address(BaseModel):

    city : str
    state : str
    pin : str


class Patient(BaseModel):

    name : str
    gender : str
    age : int
    address : Address

address_dict = {'city': 'Aurangabad', 'state' : 'Maharashtra', 'pin': '431001' }

address1 = Address(**address_dict)

patient_dict = {'name': 'Shantnau', 'gender': 'male', 'age':20, 'address': address1}

patient1 = Patient(**patient_dict)


temp = patient1.model_dump(include=['name','age'])

print(temp)
print(type(temp))


temp = patient1.model_dump_json(exclude=['name','age'])

print(temp)
print(type(temp))


temp = patient1.model_dump(exclude={'address':['city']})

print(temp)
print(type(temp))

