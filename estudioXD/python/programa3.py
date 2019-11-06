#condicionales en python
a = 100;
b = 54;

if(a>b):
    print('a es mayor de b') 
else:
    print('b es mayor que a')

if(a == b):
    print('son iguales')
else:
    print('son diferentes')

#.........................................................#
print('....')
x = 100;
y = 100;

if(x>y):
    print('x es mayor que y')
elif(a == b):
    print('son iguales')
else:
    print('y es mayor que x')
#.........................................................#
print('........')
h = 5
k = 200
#forma corta
print(h) if h > k else print(k)
#.........................................................#

#pruebe que r es mayor que u y que t es mayor que r
print('.......................')
r = 100
u = 70 
t = 200

if (r>u and t>r):
    print('es correcto afirmar que r > u y que t > r')
#........................................................#
#anidados
print('.............')
s = 100
if(s>20):
    print('es mayor de 20')
    if(s>50):
        print('y tambien es mayor de 50!!')
    else:
        print('pero no mayor de 50')

print('............')






