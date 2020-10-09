# Le preguntamos la edad al usuario
edad = int(input("¿Cual es tu edad? : "))

# Es mayor de edad
# IF en inglés significa SI
# ELSE en inglés significa SINO

# Lo que hacemos aca, es asignarle un estado
# booleano a la variable edad, es decir
# le decis que es True o 1 si tiene 18 o más
# le decis que es False o 0 si tiene menos de 18
if edad >= 18:
    status = True
else:
    status = False
    
# Acá lo que hacemos es verificar que si
# el estado es True, es mayor de edad y sino
# Es menor.
if status == True:
    print("Vos sos mayor de edad.")
else:
    print("Vos sos menor de edad")
