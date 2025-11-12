# @app.get("/patient/{patient_id}")
# def view_patient(patient_id : str = Path(..., description="ENter patient id here", example = "P002")):
#     data = load_data()

#     if patient_id in data:
#         return data[patient_id]
#     raise HTTPException(status_code=404, detail='Error id, enter valid id')



# @app.get("/sort")
# def sort_patient(sort_by : str = Query(..., description="sort on the basis of height, weight and bmi"), order_by: str=Query("asc", description="Sort on the basis of ascending or descenidng order")):

#     valid_fields = ['height', 'weight', 'bmi']

#     if sort_by not in valid_fields:
#         raise HTTPException(status_code=404, description = f"Invalid field, select from {valid_fields}")
    
#     if order not in ['asc', 'descc']:
#         raise HTTPException(status_code=400, description= "Invalid sorting order, select from ascending or descending")
    
#     data = load_data()

#     sorted_order = True if order =='desc' else False

#     sorted_data = sorted(data.values(), key= lambda x: x.get(sort_by, 0), reverse= sorted_order)

#     return sorted_data