#Variables 
#podemos uar comillas dobles o simples
#se distinguen entre mayúscula y minúscula
x = 5
y = "Hello, World!" 
Y = 'hola, mundo!'

print(x)
print(y)

# especificamos el tipo de variable
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#para saber el tipo de variable usamos la funcion type()
x = 5
y = "John"
print(type(x))
print(type(y))

#Mostramos mensaje en patalla
print ("hola tu!")

 #creamos varuable y mostramos en pantalla
n = 'juan'
print("tu nombre es: " + n)

#Multiples valores para multiples variables 
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#multiples variables un valor
x = y = z = "Orange"
print(x)
print(y)
print(z)

#lista de valores
fruits = ["apple", "banana", "cherry"]
#desempaquetamos lista
x, y, z = fruits
#mostramos valores de la lista 
print(x)
print(y)
print(z)

#Mostrar multiples variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#concatenar salida de variables
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#hacer operaciones con variables
x = 5
y = 10
print(x + y)

#Variables GLOBALES son las creadas fuera de una función 
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#creando variable dentron de una funcion con el mismo nombre de variable global

x = "awesome" #Variable GLOBAL

def myfunc():
  x = "fantastic"  #variable local solo puede ser uada dentro de la función
  print("Python is " + x)

myfunc()

print("Python is " + x)

#creando variable global dentro de una función
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
