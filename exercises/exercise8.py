"""Diccionarios"""


"""
Definir un diccionario para un 'Cliente' que contenga los siguiente valores:
- Clave "Nombre", valor de tipo string: "Mario Pedernera"
- Clave "DNI", valor de tipo integer: 56895632
- Clave "Domicilio", valor de tipo string: Los alamos 4509"
- Clave "Compras", valor de tipo lista: ["cafetera", "TV 50 pulgadas", "mouse gamer"]
"""

Cliente= {
    "Nombre":"Mario Pedernera",
    "DNI":56895632,
    "Domicilio":"Los alamos 4509",
    "Compras":["cafetera", "TV 50 pulgadas", "mouse gamer"]
}

assert (
    (Cliente["Nombre"] == "Mario Pedernera")
    and (Cliente["DNI"] == 56895632)
    and (Cliente["Domicilio"] == "Los alamos 4509")
    and (Cliente["Compras"] == ["cafetera", "TV 50 pulgadas", "mouse gamer"])
)

print (Cliente)


"""
Definir un diccionario para las 'Compras' que contenga los siguiente valores:
- Clave "Mario Pedernera", valor de tipo lista: ["cafetera", "TV 50 pulgadas", "mouse gamer"]
- Clave "Ezequiel Castello", valor de tipo lista: ["ipad", "ipod", "iphone"]
- Clave "Pablo Piristrelli", valor de tipo lista: ["Reproductor de CD", "Videograbadora"]
"""

Compras={
    "Mario Pedernera":["cafetera", "TV 50 pulgads", "mouse gamer"],
    "Ezequiel Castello":["ipad", "ipod", "iphone"],
    "Pablo Piristrelli":["Reproductor de CD", "Videograbadora"]
}


assert (
    (Compras["Mario Pedernera"] == ["cafetera", "TV 50 pulgads", "mouse gamer"])
    and (Compras["Ezequiel Castello"] == ["ipad", "ipod", "iphone"])
    and (Compras["Pablo Piristrelli"] == ["Reproductor de CD", "Videograbadora"])
)


print (Compras)

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

clave1 = diccionario.get("clave1")

assert clave1 == 234

print (clave1)


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

clave5 =(diccionario_2.get('clave4'))
clave5 = clave5[4]

assert clave5 == 5

print (clave5)


"""
Dado el siguiente diccionario obtener una lista de todas sus claves por medio del método keys
"""

diccionario_3 = {
    "clave1": 1234,
    "clave2": True,
    "clave3": "Valor 1",
    "clave4": [1, 2, 3, 4],
}

keys = list(diccionario_3.keys())

assert keys == ["clave1", "clave2", "clave3", "clave4"]

print (keys)


"""
Dado el siguiente diccionario obtener una lista de todas sus valores por medio del método values
"""

diccionario_4 = {
    "clave1": 1234,
    "clave2": 4567,
    "clave3": 8910,
    "clave4": 1112,
}

values = list(diccionario_4.values())

assert values == [1234, 4567, 8910, 1112]

print (values)


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

items = list(diccionario_5.items())

assert items == [(1, 1111), (2, 2222), (3, 3333), (4, 4444)]

print (items)


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

diccionario_6.update(diccionario_7)


assert diccionario_6 == {1: 1111, 2: 2223, 3: 3334, 4: 4444, 5: 5555, 6: 6666}

print (diccionario_6)