"""Listas"""

"""
Inicializar una lista vacía y luego agregarle 4 elementos cualquiera
Restricción: Utilizar el método append
"""

lista_01 = []
lista_01.append(8)
lista_01.append(11)
lista_01.append(18)
lista_01.append(20)

assert len(lista_01) == 4




"""
Extraer el cuarto elemento de la lista
Restricción: Utilizar el método pop
"""

lista = ["ho", "la", 81, 6, 42, "como", "estas?"]

elemento_extraido=lista.pop(3)

assert elemento_extraido == 6

print (elemento_extraido)


"""
Concatenar las siguientes listas
Restricción: Utilizar el método extend
"""

lista_a = [1, 2, 3]
lista_b = ["4", "5", "6"]
lista_c = ["siete", "ocho", "nueve"]

listas_concatenadas_01=[]
listas_concatenadas_01.extend(lista_a)
listas_concatenadas_01.extend(lista_b)
listas_concatenadas_01.extend(lista_c)


assert listas_concatenadas_01 == [1, 2, 3, "4", "5", "6", "siete", "ocho", "nueve"]

print(listas_concatenadas_01)


"""
Agregar la variable variable_01 en la tercer posición de la lista lista_nueva
Restricción: Utilizar el método insert
"""

variable_01 = 2
lista_nueva = [0, 1, 3, 4]

lista_nueva.insert(2,variable_01)

assert lista_nueva == [0, 1, 2, 3, 4]

print (lista_nueva)


"""
Armar una lista que contenga el primer y el último elemento de la siguiente lista
Restricción: Utilizar el método append junto al indexado simple
"""

lista = ["ho", 3.1416, 42, 81, 6, "la"]

lista_primero_y_ultimo = []
lista_primero_y_ultimo.append(lista[0])
lista_primero_y_ultimo.append(lista[-1])

assert lista_primero_y_ultimo == ["ho", "la"]

print (lista_primero_y_ultimo)


"""
Armar una lista que contenga los primeros 3 elementos de la siguiente lista
Restricción: Utilizar el método append junto al indexado simple
"""

lista = ["ho", 3.1416, "la", 81, 6, 42]

lista_primeros = []
lista_primeros.append(lista[0])
lista_primeros.append(lista[1])
lista_primeros.append(lista[2])

assert lista_primeros == ["ho", 3.1416, "la"]

print (lista_primeros)


"""
Armar una lista que contenga los primeros 3 elementos de la siguiente lista
Restricción: Utilizar indexado múltiple
"""

lista = ["ho", 3.1416, "la", 81, 6, 42]

lista_primeros = []
lista_primeros = lista[0:3]

assert lista_primeros == ["ho", 3.1416, "la"]

print (lista_primeros)


"""
Armar una lista que contenga los primeros 2 y los últimos 2 elementos de la
siguiente lista
Restricción: Utilizar el método extend junto al indexado múltiple
"""

lista = ["ho", "la", 81, 6, 42, "como", "estas?"]

lista_primeros_y_ultimos=[]
lista_primeros_y_ultimos.extend(lista[0:2])
lista_primeros_y_ultimos.extend(lista[5:7])

assert lista_primeros_y_ultimos == ["ho", "la", "como", "estas?"]

print(lista_primeros_y_ultimos)


"""
Concatenar las siguientes 2 listas
Restricción: Utiliar el operador +
"""

lista_01 = [0, 1, 2, 3]
lista_02 = [5, 6]

lista_concatenada = lista_01 + lista_02

assert lista_concatenada == [0, 1, 2, 3, 5, 6]

print (lista_concatenada)


"""
Concatenar 3 veces la siguiente lisa consigo misma
Restricción: Utiliar el operador *
"""

lista_01 = [0, 1, 0, 1, 0, 1]

lista_duplicada = lista_01*3

assert lista_duplicada == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

print (lista_duplicada)


"""
Verificar si el siguiente elemento pertenece a la lista
Restricción: Utiliar el operador in
"""

elemento = 1.0
lista = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1.0, 1, 0, 1, 0, 1]

variable_booleana = elemento in lista

assert variable_booleana

print (variable_booleana)



"""
Verificar si las siguientes listas son iguales
Restricción: Utilizar el operador ==
"""

lista_01 = [1, 2, 3, 4.5, 6, 7]
lista_02 = [1, 3, 2, 4, 5, 6, 7]

son_iguales = lista_01 == lista_02

assert not son_iguales

print(son_iguales)


"""
Se cuenta con una lista de elementos booleanos que corresponden a las notas de los exámenes
cuatrimestrales de un alumno (True si está aprobado y False en caso contrario)
Determinar si el alumno no tiene examenes aprobados.
Restricción: Utilizar el método any
"""

notas = [False, False, False, False, False, False, False, False, False]

no_tiene_examenes_aprobados = not any(notas)

assert no_tiene_examenes_aprobados

print (no_tiene_examenes_aprobados)


"""
Se cuenta con una lista de elementos booleanos que corresponden a las notas de los exámenes
cuatrimestrales de un alumno (True si está aprobado y False en caso contrario)
Determinar si el alumno ha aprobado todos sus exámenes.
Restricción: Utilizar el método all
"""

notas = [True, True, False, True, True, True, True, True, True, True, True, True]

tiene_todo_aprobado = all(notas)

assert not tiene_todo_aprobado

print (tiene_todo_aprobado)