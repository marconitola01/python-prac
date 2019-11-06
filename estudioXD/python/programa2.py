#imprime fecha actual
import datetime

#imprime todos los datos de fecha y hora
x = datetime.datetime.now()
print(x)

#imprime año y el nombre del dia de la semana
print(x.year)
print(x.strftime('%A'))

