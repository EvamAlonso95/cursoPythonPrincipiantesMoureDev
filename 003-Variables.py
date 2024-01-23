#VARIABLES
'''
Normas de nomenclatura de las variables
- Se recomienda escribirlas en mínusculas
- Formato snake_case
- Debe empezar por una letra o por barra baja
- No puede empezar por un número
- Solo puede contener caracteres alfanuméricos y barras baja
- Son case-sensitive
'''

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

#Tipar - casting

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

print(my_string_variable,my_int_to_str_variable,my_bool_variable)

#Concatenación de variables en un print
print(my_string_variable,my_int_variable,my_bool_variable)
print("Este es el valor de:",my_bool_variable)


#Funciones precargadas del sistema

print(len(my_string_variable)) #Cuenata los caracteres

#Variables en una sola línea - NO ES BUENA PRÁCTICA
name, surname, alias, age = "Eva", "Alonso", "Momocotón", 28

print("Me llamo:",name,surname,". Mi edad es:",age,". Y mi alias es:",alias)

#Input() - entrada de datos

'''
name = input('¿Cuál es tu nombre: ')      #Sobreescribimos el valor name
age = input('¿Cuántos años tienes? ')     #Sobreescribimos el valor age
'''

print(name)
print(age)

#Python no tiene un tipado fuerte. Se puede cambiar los valores sin problema
name = 35
age = "Momo"

print(name)
print(age)


#¿Forzamos el tipo?
adress: str = "Mi dirección" #Esto es para ayudarnos a nosotros, realmente no fuerza nada 
adress = 32
print(adress) # int

#Nos devuelve las palabras reservadas de python
help('keywords')

#EJERCICIOS 
#LEVEL 1
# 'Day 2: 30 Days of python programming'
first_name = "Margarita"
last_name = "Flores"
full_name = first_name +" "+ last_name

print(full_name)

country = "España"
city = "Asturias"
age = 25
year = 2024
is_married = False
is_true = False
is_light_on = False

color, hobbie, food, born_year, have_car =  "red", "do skate", "sushi", 1995, True

print(color, hobbie, food, born_year, have_car)

#LEVEL 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(color))
print(type(hobbie))
print(type(food))
print(type(born_year))
print(type(have_car))

print(len(first_name))
print(len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two
print(total)

diff = num_one - num_two
print(diff)

product = num_one * num_two
print(product)

division = num_one / num_two
print(division)

remainder = divmod(num_two, num_one) #cociente y modulo / resto
print(remainder)

exp = num_one**num_two
print(exp)

floor_division = num_one // num_two
print(floor_division)

radius = int(input("Dime el radio de la circunferencia:"))
area_of_circle = 3.14*(radius**2)
print("El area es:", area_of_circle)

circum_of_circle = (3.14*2)*30
print("La circunferencia es:", circum_of_circle)

first_name = input("Nombre:")
last_name =input("Apellido:")
country = input("País:")
age = input("Edad:")