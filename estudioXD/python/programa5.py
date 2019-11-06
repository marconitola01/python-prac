#listas o arreglos de python
lista1 =[]
print('cuantos elementos va a guardar?')
cantidad = int(input())


for x in range (cantidad):
    print('ingrese un elemento')
    lista1.append(input('dame un elemento'))

print(lista1)

#..................................
#comprobar si el elemento existe
lista2 =[2,3,4,5]
print('ingrese numero a buscar')
Buscar = int(input())
if(Buscar in lista2):
    print('si existe')
else:
    print('no existe')
    
#.................................
#longitud de la lista
print('el tamaño de la lista2 es = ',len(lista2))
#.................................
#eliminar elemento especificado
lista3 = ['cerveza','perico','cigarrillo']
print('original: ',lista3)
lista3.remove('cerveza')
print('cambiado: ',lista3)

#invertir una lista o arreglo
listaNUM = [1,2,3,4,5,6,7,8,]
print('lista original',listaNUM)
listaNUM.reverse()
print('lista invertida',listaNUM)

#rellenar un array con caracteres

listaChar = []
print('cuantos caracteres va a ingresar?')
cantidad2 = int(input())

for x in range(cantidad2):
    print('ingresa un caracter')
    listaChar.append(input())
print('la lista esta asi: ',listaChar)
listaChar.reverse()
print('la lista inversa',listaChar)





        


