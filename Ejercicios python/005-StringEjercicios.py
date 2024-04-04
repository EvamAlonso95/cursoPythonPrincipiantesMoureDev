#1
a = "treinta"
b = "días"
c = "de"
d = "Python"

tituloCurso = a +" "+ b +" "+ c+" "+ d
print(tituloCurso)


#2

e = "Programación"
f = "para"
g = "todos"

fraseMotivacional = e +" "+ f + " " + g
print(fraseMotivacional)

#3 y 4

company = fraseMotivacional
print(company)

#5 
print(len(company))

#6

print(company.upper())

#7

print(company.lower())

#8
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9

#print(company.strip("Programación"))

#10
print(company.find("Programación"))
print(company.find("para"))

#11
company = company.replace("Programación", "Pyhton")
print(company)
print(company.replace("todos", "todo el mundo"))

#13
print(company.split())

#14
browsers = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
result = browsers.split(",")
print(result)

#15  16 17 18 19
print(company[0])
print(company[-1])
print(company[10])
print(company[0:3])

#20
print(company.index("P"))
print(company.index("t"))
print(company.index("o"))

#23 24
sentence = "You cannot end a sentence with because because because is a conjunction"

print(sentence.find("because"))
print(sentence.index("because"))

print(sentence.rindex("because"))

print(sentence.replace("because",""))

#28 29
print(company)

print(company.startswith("Pyhton"))
print(company.endswith("Pyhton"))

#30
spaceCompany = '   Coding For All      .' 
print(spaceCompany)
print(spaceCompany.replace(" ",""))

#31 El método isidentifier() en Python se utiliza para verificar si una cadena es un identificador válido en Python o no. Un identificador válido en Python es un nombre que puede ser utilizado para nombrar variables, funciones, clases, etc.
var1 = "30DaysOfPython"
var2 = "thirty_days_of_python"
print(var1.isidentifier())
print(var2.isidentifier())

#32
list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

joinList = "# ".join(list)

print(joinList)

#33
print("I am enjoying this challenge.\nI just wonder what is next.")
#34
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

#35
radius = 10
area = 3.14 * radius ** 2
formated_string = 'El área de un círculo con área {} es {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

#36
a = 8
b = 6

print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

