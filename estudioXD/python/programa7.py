def papu():
    print('papu')

papu()

def factorial(numero):
    facto = 1;
    while(numero > 1):
        facto = facto*numero
        numero = numero - 1
    return facto

print('ingrese numero a operar')
numero = int(input())
print('el factorial de',numero,'es: ',factorial(numero))
