def prueba(y):
    print("se esta ejecutando la prueba")
    if y == 1:
        y = y+1
        print("y = 1 y se le suma 1 =",y)
    else:
        y = y + 2
        print("y != 1, se le suma 2=",y)
    return y #prueba(b) es sustituido por y
def suma(a,b):
    sum = a + b
    return sum
print("1 is an int and" + " " + "Hello world is a string")
a=1
x = 1 + 2 * 3 - 8 / 4
print(x)
print(int(98.6))
while a <= 5:
    print("hello world")
    a= a+1
b = 5 / 2
print(b)
pregunta = input("¿Quién eres?\n")
if pregunta != "Adrián":
    print("No eres Adrián, vete.")
else:
    print("Ah vale, bienvenido.")
y = 2
print(y)
prueba(y)
print(prueba(y))
i=5
j=4
resultado = suma(i,j)
print(resultado)
print(suma(4,5))
personas = ["Adrian","Cristina","Asier","Jara"]
for persona in personas: #se recorre(itera) un array
    print("Feliz año",persona)
zork =0
for thing in [9,3,2]:
    zork = zork + thing
print(zork)
w = 5 #operadores lógicos or not() y and
if w == 8 or w == 5: # más de una opcion en el if 
    print("pasa")
else:
    print("no pasa")

