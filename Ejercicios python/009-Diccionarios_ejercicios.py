#1

dog = {}

#2

dog = {
    "Nombre":"Toby", "Raza":"Beagle", "color":"Marrón", "Edad":7
}
print(dog)
#3
student = {
    "first_name":"Louis", "last_name":"Logan", "gender":"Male", "age":25, "marital status":"in a relationship", "skills":["Javascript","html","css"], "country":"Spain", "city":"barcelona", "address":"Calle de la piruleta" 
}

#4
print(len(student))
#5
# list_student = student.get("skills")
# print(list_student)
# print(type(list_student))
#6
student['skills'].append('HTML')
student['skills'].append('CSS')

print(student)
#7
print(student.keys())
#8
print(student.values())
#9
student_list = student.items()
print(type(student_list))
#10
student.pop("skills")
print(student)
#11
del student
print(student)