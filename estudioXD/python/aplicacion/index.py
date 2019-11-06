from tkinter import ttk
from tkinter import *

class producto:
    def __init__(self,window):
        self.wind = window
        self.wind.title('aplicacion de productos')

    def productos(self):
        self.id = ''
        self.nombre = ''
        self.cantidad = ''
        self.precio = ''
        self.disponible



if __name__ == "__main__":
    window = Tk()
    aplicacion = producto(window)
    window.mainloop()