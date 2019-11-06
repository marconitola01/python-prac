"""
#pedir datos de un cuadrado y dibujarlo
def dibujo(altura,ancho):
    for i in range (altura):
        for j in range(ancho):
            print("*", end="")
        print()

print('ingrese altura')
altura = int(input())
print ('ingrese ancho')
ancho = int(input())

dibujo(altura,ancho)

#con caracter de preferencia para el usuario
def dibujo2(caracter, altura, ancho):
    for i in range (altura):
        for j in range (ancho):
            print(caracter, end="")
        print()

print('ingrese la altura')
altura = int(input())
print('ingrese el ancho')
ancho = int(input())
print('ingrese el caracter que desea en el dibujo')
caracter = input()
dibujo2(caracter,altura,ancho)    

#comprobar año biciesto

def Añobiciesto(año):
    if(año % 4 == 0 or (año % 100 !=0 and año % 400 == 0)):
        print('el año: ',año,'es año biciesto')
    else:
        print('el año: ',año,'no es un año biciesto')

print('ingrese un año y le dire si es biciesto o no')
año = int(input())
Añobiciesto(año)

#CREAR UNA LISTA DE PALABRAS

def CreadorListas():
    lista = []
    print('cuantas palabras tendra la lista?')
    cantidad = int(input())
    for i in range (cantidad):
        print('ingrese una palabra')
        palabra = input()
        lista.append(palabra)
    print('esta es su lista',lista)

CreadorListas()
"""""
#creadro de las listas que desee el user

def CreadorListas2(contador):
    Lista2 = []
    print('¿cuantas palabras tendra la lista?')
    cantidad = int(input())
    for j in range (cantidad):
        print('ingrese una palabra')
        palabra = input()
        Lista2.append(palabra)
    return Lista2
   
   


print('cuantas listas quiere?')
cantidadLis=int(input())

for i in range (1, cantidadLis + 1):
    print('la lista ',i, 'es: ',CreadorListas2(i))


