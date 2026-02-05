student = {
    "name": "Aiman",
     "course": "MCA", 
     "college": "UBDT"
     }
print(student["name"])
print(student["course"])
print(student["college"])

student = {
    "name": "sheikh naaz",
    "age": 22,
    "course": "MCA",
    "id": "4UBMC002"
    }
print(student["name"])
student["age"]=24
print(student["age"])
print(student["id"])
student["city"]="Chitradurga"
print(student["city"])
print(student.keys())
student.pop("age")
print(student)
