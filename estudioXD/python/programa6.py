#maximo de dos numeros
def maximo(var1,var2):
    if(var1>var2):
        print('el elemento uno es mayor del elemento dos')
    else:
        print('el elemento dos es mayor')

    if(var1 == var2):
        print('son iguales')

print('ingrese elemento uno')
var1 = int(input())
print('ingrese el elemento dos')
var2 = int(input())

maximo(var1,var2)

#maximo de tres numeros
def maximo2(var1,var2,var3):
    if(var1>var2 and var1 > var3):
        print('el mayor es el elemento uno')
    elif(var2>var1 and var2>var3):
        print('el mayor es el elemento dos')
    elif(var3>var1 and var3>var2):
        print('el mayor es el elemento tres')
        
print('ingrese numero uno')
var1 = int(input())
print('ingrese numero dos')
var2 = int(input())
print('ingrese numero tres')
var3 = int(input())
maximo2(var1,var2,var3)

#longitud de una lista sin usar len()
lista = [2,2,2,2,2,2,2]
def largoLista(lista):
    contador = 0
    for i in lista:
        contador += i
    return contador

print(largoLista(lista))

#devolver si es una vocal o no

def Vocal(x):
    if(x == 'a' or x=='e' or x=='i' or x=='o' or x=='u'):
        print('es una vocal')
    elif(x == 'A' or x=='E' or x=='I' or x=='O' or x=='U'):
        print('es una vocal')
    else:
        print('no es vocal')
print('ingrese el caracter a validar')
x = input()
Vocal(x)

#sumar el multiplixar todos los numeros de una misma lista

def suma(lista):
    suma = 0;
    for i in lista:
        suma += i
    return suma
def multiplicacion(lista):
    multi = 1
    for i in lista:
        multi *= i
    return multi
lista = [2,2,2]    
print('la suma da: ',suma(lista))
print('la multiplicacion da: ',multiplicacion(lista))

#invertir una cadena

def invertir(cadena):
    cadenainvertida = cadena[::-1]
    return cadenainvertida

print('ingrese palabra a invertir')
cadena = input()
print(invertir(cadena))

#palindromo

def palindromo(cadena):
    inverso = cadena[::-1]
    if(cadena == inverso):
        print ('es un palindromo')
    else:
        print('no es palindromo')
print('ingrese una palabra para ver si es palindromo o no')
cadena = input()

palindromo(cadena)

#factorial de un numero
def factorial(numero):
    facto = 1;
    while numero > 1:
        facto *= numero
        numero -= 1
    return facto 
print('ingrese un numero')
numero = int(input())

print('factorial = ', factorial(numero))





        