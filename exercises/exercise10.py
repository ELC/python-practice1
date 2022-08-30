"""Coerción a Booleanos"""


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_01
"""

A = 5

# COMPLETAR - INICIO
variable_01 = bool(A)
# COMPLETAR - FIN

assert variable_01 is True


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_02
"""

Domicilio = ""

# COMPLETAR - INICIO
variable_02 = bool(Domicilio)
# COMPLETAR - FIN

assert variable_02 is False


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_03
"""

Domicilio = "Alsina 2446" or "Pueyrredón y la vía"

# COMPLETAR - INICIO
variable_03 = bool(Domicilio)
# COMPLETAR - FIN

assert variable_03 is True


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_04
"""

lista_de_compras = "No comprar nada" and ["Pan", "Aceite", "Sal"]

# COMPLETAR - INICIO
variable_04 = bool(lista_de_compras)
# COMPLETAR - FIN

assert variable_04 is True


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_05
"""

lista_de_ids = 0 and [1236, 5565, 8956, 2534]

# COMPLETAR - INICIO
variable_05 = bool(lista_de_ids)
# COMPLETAR - FIN

assert variable_05 is False


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_06
"""

diccionario = {} and {"Nombre": "Alberto Paz", "DNI": 12365855}

# COMPLETAR - INICIO
variable_06 = bool(diccionario)
# COMPLETAR - FIN

assert variable_06 is False