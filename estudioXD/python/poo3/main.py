#clase padre Vehiculos
class Vehiculos():
    #estado inicial de las variables
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.frena = False
        self.acelera = False
    #metodos acelerar, frenar, arrancar, estado
    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def arrancar(self):
        self.enmarcha = True

    def estado(self):
        print(' modelo: ',self.modelo, '\n marca: ',self.marca,'\n acelera:',self.acelera,'\n frena: ',self.frena,'\n en marcha: ',self.enmarcha,'\n')

#soporte para vehiculos electricos
class Velectricos():
    def __init__(self):
        self.autonomia = 100

    def cargarBateria(self):
        self.cargando = True
        

#clase moto que hereda de la clase padre Vehiculos
class moto(Vehiculos):
    caballito = ""
    def hcaballito(self):
        self.caballito = 'voy haciendo el caballito'

    def estado(self):
        print(' modelo: ',self.modelo, '\n marca: ',self.marca,'\n acelera:',self.acelera,'\n frena: ',self.frena,'\n en marcha: ',self.enmarcha,'\n',self.caballito)
#clase furgoneta que hereda de la clase vehiculos
class furgoneta(Vehiculos):
    def carga(self,cargar):
        self.cargado = cargar
        if(self.cargado):
            return 'la furgoneta esta cargada'
        else:
            return 'la furgoneta esta vacia'
        
#clase bicielectrica que herada tanto de velectricos y de vehiculos
class bicielectrica(Velectricos,Vehiculos):
    pass

#clase de lamborghinis
class Lamborghini():
    pass



#instancias de la clase moto
miMoto = moto('yamaha','r15')
miMoto.arrancar()
miMoto.acelerar()
miMoto.hcaballito()
miMoto.estado()
#instancias de la clase furgoneta
print('............................vehiculo dos.........................................')
miFurgon = furgoneta('chevrolet','npr200')
miFurgon.arrancar()
miFurgon.acelerar()
miFurgon.estado()
print(miFurgon.carga(False))
#instancias para  la clase bici electrica
#como el constructor de velectricos esta de primero se le da prioridad y los argumentos del contrctor vehiculos no sirve
#miBici = bicielectrica('orbea','h1000')
miBici = bicielectrica(); #sin argumentos porque el contructor no los pide





    
