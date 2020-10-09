# Estos son metodos que pueden aplicarse en el uso de diccionarios.

# Primero declaramos un diccionario, de la siguiente manera
diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript'] }

# Luego accedemos a los elementos del diccionario, asi
print diccionario['nombre']     #Carlos
print diccionario['edad']       #22
print diccionario['cursos']     #['Python','Django','JavaScript']

# Ahora probamos insertar elementos en el diccionario, probando los indices
print diccionario['cursos'][0]#Python
print diccionario['cursos'][1]#Django
print diccionario['cursos'][2]#JavaScript

# Podemos recorrer un diccionario de la siguiente manera
for key in diccionario:
    print key, ":", diccionario[key]

# dict() = Recibe como parámetro una representación de un diccionario y si es factible, 
# devuelve un diccionario de datos.
dic =  dict(nombre='nestor', apellido='Plasencia', edad=22)

# zip() = Recibe como parámetro dos elementos iterables, ya sea una cadena, una lista o una tupla. 
# Ambos parámetros deben tener el mismo número de elementos. 
# Se devolverá un diccionario relacionando el elemento i-esimo de cada uno de los iterables.
dic = dict(zip('abcd',[1,2,3,4]))

# items() = Devuelve una lista de tuplas, cada tupla se compone de dos elementos: el primero será la clave y el segundo, su valor.
dic = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
items = dic.items()

# keys() = Retorna una lista de elementos, los cuales serán las claves de nuestro diccionario.
dic =  {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
keys= dic.keys()

# values() = Retorna una lista de elementos, que serán los valores de nuestro diccionario.
dic =  {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
values= dic.values()

# clear() = Elimina todos los ítems del diccionario dejándolo vacío.
dic 1 =  {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
dic1.clear()

# copy() = Retorna una copia del diccionario original.
dic = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
dic1 = dic.copy()

# fromkeys() = Recibe como parámetros un iterable y un valor, 
# devolviendo un diccionario que contiene como claves los elementos del iterable con el mismo valor ingresado. 
# Si el valor no es ingresado, devolverá none para todas las claves.
dic = dict.fromkeys(['a','b','c','d'],1)

# get() = Recibe como parámetro una clave, devuelve el valor de la clave. Si no lo encuentra, devuelve un objeto none.
dic = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
valor = dic.get(‘b’) 

# pop() = Recibe como parámetro una clave, elimina esta y devuelve su valor. Si no lo encuentra, devuelve error.
dic = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
valor = dic.pop(‘b’) 

# setdefault() = Funciona de dos formas. En la primera como get
dic = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
valor = dic.setdefault(‘a’)

# Y en la segunda forma, nos sirve para agregar un nuevo elemento a nuestro diccionario.

dic = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
valor = dic.setdefault(‘e’,5)

# update() = Recibe como parámetro otro diccionario. Si se tienen claves iguales, actualiza el valor de la clave repetida; si no hay claves iguales, este par clave-valor es agregado al diccionario.
dic 1 = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
dic 2 = {‘c’ : 6, ’b’ : 5, ‘e’ : 9 , ‘f’ : 10}
dic1.update(dic 2)
