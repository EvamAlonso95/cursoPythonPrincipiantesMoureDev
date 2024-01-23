#OPERADORES

#Básicos
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)

#Intermedios
print(10 % 2)  #Nos da el resto de la división
print(10 // 3) #Floor division - Nos da el resultado aproximado
print(10 ** 2) #Exponente
print(10 ** 2 + 3 - 2 /2)
#Con cadenas de texto
print("Hola "+"Python "+"¿Qué tal?") 
# print("Hola"-"Python") - ERROR
# print("Hola"+ 5) - No podemos mezclar tipos 
print("Hola "+ str(5))
print("Hola"* 5) #Multiplicamos las veces que nos lo imprime
print("Hola\n"* (2 ** 3))

my_float = 2.5 *2 #float
print("Hola " * int(my_float))
print("///////////////")

#Operadores comparativos
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print("///////////////")
#Se están comparando en una ordenación alfabética por ASCII
print("Hola" > "Python")
print("Hola"  < "Python")
print("Hola"  >= "Python")
print("Hola"  <= "Python")
print("Hola"  == "Hola")
print("Hola"  != "Python")
print("aaaa" > "bbbb")
print(len("aaaa") > len("bbbb")) #Compara caracteres

#Operadores lógicos

print(3 > 4 and "Hola" > "Python") #False y False = False
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python") #True y True = True
print(3 < 4 or "Hola" > "Python")  #True o False = True
print(3 < 4 or "Hola" > "Python" and 4 == 4)
print(not(3 > 4) ) # 3 > 4 es falso, pero al negarlo es True. 3 > 4 Negamos la condición

#PLUS
# In addition to the above comparison operator Python uses:

# is: Returns true if both variables are the same object(x is y)
# is not: Returns true if both variables are not the same object(x is not y)
# in: Returns True if the queried list contains a certain item(x in y)
# not in: Returns True if the queried list doesn't have a certain item(x in y)

print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all')       # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')            # True
print('4 is 2 ** 2:', 4 is 2 ** 2)        # True

#EJERCICIOS 
#LEVEL 1
my_age = 28
my_height = 1.62
complex_number = 1 + 1j

base = int(input("Introduce la base del triángulo:"))
height = int(input("Introduce la altura del triángulo:"))
area_of_triangle = (base * height)/2
print("El área del triángulo es: ", area_of_triangle)

side_a = int(input("Introduce la medida del lado a:"))
side_b = int(input("Introduce la medida del lado b:"))
side_c = int(input("Introduce la medida del lado c:"))
perimeter_of_triangle = side_a + side_b + side_c
print("El perímetro del triángulo es:", perimeter_of_triangle )

lengt_rectangle =  int(input("Introduce la altura:"))
width_rectangle = int(input("Introduce el ancho:"))
area_of_rectangle = lengt_rectangle*width_rectangle
perimeter_of_rectangle = 2*(lengt_rectangle+width_rectangle)
print("El área del rectángulo es:",area_of_rectangle," y el perímetro del rectángulo es:",perimeter_of_rectangle)

pi = 3.14
radius_of_circle = int(input("Introduce el radio:"))
area_of_circle = pi*radius_of_circle*radius_of_circle
circumference_of_circle = 2*pi*radius_of_circle
print("El area de un círculo es", area_of_circle, "y la circunferencia es:",circumference_of_circle)

python_len = len("python")
dragon_len = len("dragon")

print(python_len)
print(dragon_len)

print(dragon_len!=python_len)

print("gon"  in "dragon" and  "gon" in "python")

print("jargon" in "I hope this course is not full of jargon")

print("on"  not in "dragon" and  "on" not in "python")

float_python_len = float(python_len)
print(type(float_python_len))
string_python_len = str(float_python_len)
print(type(string_python_len))

number = int(input("Introduce un número:"))
resto = number % 2
print(resto == 0)

floor_division = 7 // 3
value_converted = int(2.7) 
print(floor_division == value_converted) #True 
print(floor_division)
print(value_converted)

print(type('10') == type (10)) #False

print (int(9.8)==10) #False

hours = int(input("Horas trabajadas:"))
rate_per_hour = int(input("Dinero por hora:"))
weekly_earning =(hours*rate_per_hour)
print("A la semana ganas:", weekly_earning)

years_lived = int(input("Introduce los años vividos:"))
seconds_lived = 31536000 * years_lived
print("You have lived for",seconds_lived," segundos")



