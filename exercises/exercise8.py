"""Diccionarios"""


"""
Definir un diccionario para un 'Cliente' que contenga los siguiente valores:
- Clave "Nombre", valor de tipo string: "Mario Pedernera"
- Clave "DNI", valor de tipo integer: 56895632
- Clave "Domicilio", valor de tipo string: Los alamos 4509"
- Clave "Compras", valor de tipo lista: ["cafetera", "TV 50 pulgadas", "mouse gamer"]
"""

# COMPLETAR - INICIO

# COMPLETAR - FIN

assert (
    (Cliente["Nombre"] == "Mario Pedernera")
    and (Cliente["DNI"] == 56895632)
    and (Cliente["Domicilio"] == "Los alamos 4509")
    and (Cliente["Compras"] == ["cafetera", "TV 50 pulgadas", "mouse gamer"])
)


"""
Definir un diccionario para las 'Compras' que contenga los siguiente valores:
- Clave "Mario Pedernera", valor de tipo lista: ["cafetera", "TV 50 pulgadas", "mouse gamer"]
- Clave "Ezequiel Castello", valor de tipo lista: ["ipad", "ipod", "iphone"]
- Clave "Pablo Piristrelli", valor de tipo lista: ["Reproductor de CD", "Videograbadora"]
"""

# COMPLETAR - INICIO

# COMPLETAR - FIN

assert (
    (Compras["Mario Pedernera"] == ["cafetera", "TV 50 pulgads", "mouse gamer"])
    and (Compras["Ezequiel Castello"] == ["ipad", "ipod", "iphone"])
    and (Compras["Pablo Piristrelli"] == ["Reproductor de CD", "Videograbadora"])
)


"""
Dado el siguiente diccionario obtener el valor de la "clave1" utilizando el metodo get y
guardarlo en la variable clave1
"""

diccionario = {
    "clave1": 234,
    "clave2": True,
    "clave3": "Valor 1",
    "clave4": [1, 2, 3, 4],
}

# COMPLETAR - INICIO

# COMPLETAR - FIN

assert clave1 == 234


"""
Dado el siguiente diccionario forzar la obtención de un valor por defecto igual a 5 utilizando
el metodo get y almacenarlo en la variable clave5
Restricción: Se debe intentar obtener un valor para la clave inexistente "clave5"
"""

diccionario_2 = {
    "clave1": 234567,
    "clave2": False,
    "clave3": "Valor 13",
    "clave4": [1, 2, 3, 4, 5, 6],
}

# COMPLETAR - INICIO

# COMPLETAR - FIN

assert clave5 == 5


"""
Dado el siguiente diccionario obtener una lista de todas sus claves por medio del método keys
"""

diccionario_3 = {
    "clave1": 1234,
    "clave2": True,
    "clave3": "Valor 1",
    "clave4": [1, 2, 3, 4],
}

# COMPLETAR - INICIO

# COMPLETAR - FIN

assert keys == ["clave1", "clave2", "clave3", "clave4"]


"""
Dado el siguiente diccionario obtener una lista de todas sus valores por medio del método values
"""

diccionario_4 = {
    "clave1": 1234,
    "clave2": 4567,
    "clave3": 8910,
    "clave4": 1112,
}

# COMPLETAR - INICIO

# COMPLETAR - FIN

assert values == [1234, 4567, 8910, 1112]


"""
Dado el siguiente diccionario obtener una lista de sus claves y sus valores uno a continuación
de otro por medio del metodo items
"""

diccionario_5 = {
    1: 1111,
    2: 2222,
    3: 3333,
    4: 4444,
}

# COMPLETAR - INICIO

# COMPLETAR - FIN

assert items == [(1, 1111), (2, 2222), (3, 3333), (4, 4444)]


"""
Dados dos diccionarios actualizar el primero con los valores del segundo utilizando el método update
"""

diccionario_6 = {
    1: 1111,
    2: 2222,
    3: 3333,
    4: 4444,
}

diccionario_7 = {
    2: 2223,
    3: 3334,
    5: 5555,
    6: 6666,
}

# COMPLETAR - INICIO

# COMPLETAR - FIN

assert diccionario_6 == {1: 1111, 2: 2223, 3: 3334, 4: 4444, 5: 5555, 6: 6666}