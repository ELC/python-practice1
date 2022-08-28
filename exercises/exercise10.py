"""Coerción a Booleanos"""


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_01
"""

A = 5

variable_01 = bool(A)

assert variable_01 is True

print (variable_01)


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_02
"""

Domicilio = ""

variable_02 = bool(Domicilio)


assert variable_02 is False


print (variable_02)


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_03
"""

Domicilio = "Alsina 2446" or "Pueyrredón y la vía"

variable_03 = bool(Domicilio)

assert variable_03 is True


print (variable_03)


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_04
"""

lista_de_compras = "No comprar nada" and ["Pan", "Aceite", "Sal"]

variable_04 = bool(lista_de_compras)

assert variable_04 is True


print (variable_04)


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_05
"""

lista_de_ids = 0 and [1236, 5565, 8956, 2534]

variable_05 = bool(lista_de_ids)

assert variable_05 is False

print (variable_05)


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_06
"""

diccionario = {} and {"Nombre": "Alberto Paz", "DNI": 12365855}

variable_06 = bool(diccionario)

assert variable_06 is False

print (variable_06)