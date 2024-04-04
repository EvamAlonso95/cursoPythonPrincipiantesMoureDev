#Nivel 1

    #  1
# age = int(input("Introduce tu edad: "))
# if age >= 18:
#     print("Tienes edad para conducir")
# else:
#     print("No tienes edad para conducir")

    #  2
# my_age = 28
# your_age = int(input("Introduce tu edad: "))
# if my_age == your_age:
#     print("Tenemos la misma edad")
# elif my_age > your_age:
#     print("soy mayor que tu")
# else:
#     print("Tú eres mayor que yo")

    #  3
# num1 = int(input("Introduce un número: "))
# print("Has introducido el número %i" %(num1))
# num2 = int(input("Introduce un número: "))
# print("Has introducido el número %i" %(num2))

# if num1 > num2:
#     print("El número %i es mayor que el número %i" %(num1,num2))
# elif num1 < num2:
#     print("El número %i es mayor que el número %i" % (num2, num1))    
# else:
#     print("Ambos números son iguales")
    
#Nivel 2

    #  1
# grade = int(input("Introduce la nota: "))

# if grade <= 49:
#     print("Tu nota es de F")
# elif grade <= 59:
#     print("Tu nota es de D")
# elif grade <= 69:
#     print("Tu nota es de C")
# elif grade <= 79:
#     print("Tu nota es de B")
# else:
#     print("Tu nota es de A")

    #  2
# month = input("Introduce un mes: ")

# if month == "Septiembre" or month == "Octubre" or month == "Noviembre":
#     print("Estamos en otoño")
# elif month == "Diciembre" or month == "Enero" or month == "Febrero":
#     print("Estamos en invierno")
# elif month == "Marzo" or month == "Abril" or month == "Mayo":
#     print("Estamos en primavera")
# elif month == "Junio" or month == "Julio" or month == "Agosto":
#     print("Estamos en verano") 
# else:
#     print("No has introducido un mes")
    
    #  3
# fruits = ['platano', 'naranja', 'mango', 'limon']

# fruit = input("introduce una fruta:")
# fruit = fruit.lower()

# fruit_exist = fruit in fruits

# # print(fruit_exist)

# if not fruit_exist:
#     fruits.append(fruit)
#     print("La cesta ahora tiene estas frutas: ",fruits)
# else:
#     print("Esta fruta ya existe en la lista")

#Nivel 3

   
person={
    'first_name': 'Eva',
    'last_name': 'Alonso',
    'age': 28,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python' ],
    'address': {
        'calle': 'calle piruleta',
        'codigo_postal': '001122'
    }
    }

 # 1
# if 'skills' in person:
#     skills_list = person['skills']
#     middle_skills = len(skills_list) // 2
#     print(skills_list[middle_skills])

 # 2
# if 'skills' in person:
#     skills_list = person['skills']
#     result = 'Python' in skills_list
#     print(result)

 # 3
# skills = person.get('skills', [])  # Obtener la lista de habilidades, si no existe, asignar una lista vacía

# # Verificar las diferentes combinaciones de habilidades y determinar el título del desarrollador
# if skills == ['JavaScript', 'React']:
#     print('Él es un desarrollador de front-end')
# elif set(skills) == {'Node', 'Python', 'MongoDB'}:
#     print('Él es un desarrollador de back-end')
# elif set(skills) == {'React', 'Node', 'MongoDB'}:
#     print('Él es un desarrollador de full-stack')
# else:
#     print('Título desconocido')
    
   # 4

if person['is_marred']:  # Debe ser 'is_married' en lugar de 'is_marred'
    country = person.get('country')
    if country == 'Finland':
        print(person['first_name'], person['last_name'], "vive en", person['country'] + ". Ella está casada.")
