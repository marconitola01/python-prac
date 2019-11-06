def calculadora(op):
    if(op == 1):
        print('\n ingrese dos numeros')
        var1 = int(input())
        var2 = int(input())
        resultado = var1+var2 
        print('resultador =',resultado)
    elif(op == 2 ):
        print('\n ingrese dos numeros')
        var1 = int(input())
        var2 = int(input())
        resultado = var1-var2
        print('resultado =', resultado )
    elif(op == 3):
        print('\n ingrese dos numeros')
        var1 = int(input())
        var2 = int(input())
        resultado = var1*var2
        print('resutado =', resultado)
    elif(op == 4):
        print('\n ingrese dos numeros')
        var1 = int(input())
        var2 = int(input())
        resultado = var1/var2
        print('resultado =',resultado)
    elif(op == 5):
        print('ingrese un numero para sacar factorial')
        numero = int(input())
        facto = 1
        while numero > 1:
            facto *= numero
            numero -= 1
        print('resultado =',facto)
print('ingrese una opcion\n')
print('1) suma \n2) resta \n3)multiplicacion \n4)Division \n5)factorial')
opcion = int(input())

calculadora(opcion)

    
