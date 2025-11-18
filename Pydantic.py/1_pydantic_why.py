def insert_patient_data(name : str, age : int):

    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("Inserted into databases")
    else:
        raise TypeError('Invalid data types')

insert_patient_data('Shantanu', '20')



def insert_patient_data(name : str, age : int):

    if type(name) == str and type(age) == int:

        if age < 0 :
            raise ValueError("Age can not be negative.")
        else:
            print(name)
            print(age)
            print("Inserted into databases")
    else:
        raise TypeError('Invalid data types')

insert_patient_data('Shantanu', '20')


