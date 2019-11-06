#practica de poo en python alv
class Carro:
    #propiedades de la clase
    #constructor de clase __init__
    def __init__(self):
        self.__ruedas = 4 #no es accesible desde otras clases
        self.__marca = 'volvo'
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__enmarcha = False
    
    #comportamientos o metodos (dos)
    def arrancar(self,arrancar):
        self.__enmarcha= arrancar
        chequeo = self.__Chequeo_interno()
        if(self.__enmarcha and chequeo == True):
            return 'el carro esta en marcha'
        elif(self.__enmarcha and chequeo == False):
            return 'algo ha salido mal no podemos arrancar revise gasolina o aceite'
        else:
            return 'el carro esta parado'

    def estado(self):
        print('el carro tiene',self.__ruedas,'ruedas','- la marca es',self.__marca,'- el largo de chasis ',self.__largoChasis)

    def __Chequeo_interno(self): #encapsulamos el metodo para que solo sea accesible por la clase 
        print('realizando testeo interno del carro')
        gasolina = 'ok'
        aceite = 'ok'
        agua = 'not ok'
        puertas = 'cerradas'
        
        if(gasolina == 'ok' and aceite == 'ok' and agua == 'ok' and puertas == 'cerradas'):
            return True
        else:
            return False





print('..........................inicio.............................................')
miCarro = Carro() #instanciar una clase
print(miCarro.arrancar(True))
miCarro.estado()

#segundo objeto con diferentes atributos
print('..........................a continuacion creamos nuestro segundo objeto..............................')
miCarro2 = Carro()
miCarro2.ruedas=2#como esta encapsulado no podemos cambiar la variable ruedas
print(miCarro2.arrancar(False))
miCarro2.estado()


