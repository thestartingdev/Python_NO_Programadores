# Vamos a importar
# la libreria que imprime el calendario asi:
import calendar

# Ahora vamos a pedirle al usuario
# que ingrese el año que quiere ver
# declarando la variable year
year = int(input("¿Qué año queres ver? "))

# Ahora le pedimos que ingrese el mes
month = int(input("¿Y que mes? "))

# Para finalizar imprimimos
# el mes del año socilitado
print(calendar.month(year, month))