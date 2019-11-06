#tuplas no son editables pero si manejables
tupla1 = ('mazana','banano','perico','cerveza','venecas')
print(tupla1)
print('..................')
#acceder a elementos de la tupla
print('el primer elemento de la tupla = '+ tupla1[0])
print('el segundo elemento de la tupla = '+ tupla1[1])
print('el tercer elemento de la tupla = '+ tupla1[2])
print('.....................')
#indexacion negativa
print('el ultimo elemento de la tupla = '+ tupla1[-1])
#rango de indices
print(tupla1[2:4]);
print('......................')
#cambiar elementos de la tupla (como una tupla no es editable hay que convertirla en un lista)
y = list(tupla1)
y[1] = 'heroina'
tupla1 = tuple(y)

print (tupla1)
print('.................................')

#recorrer una tupla

for x in tupla1:
    print(x)

#comprobar si el elemento existe

print('ingrese el elemento a buscar')
busca = input() 
if(busca in tupla1):
    print('si existe el elemento')
else:
    print('no existe tal elemento')    

print('.............................')
#longitud de una tupla
print('elementos de la tupla = ', len(tupla1))

#unir dos tuplas
tupla2 = (2,3,4)
tupla3 = ('a','b','c')

tuplaResult = tupla2 + tupla3
print('la tubla combinacion es = ',tuplaResult)


