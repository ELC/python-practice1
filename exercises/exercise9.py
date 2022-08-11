"""Conjuntos"""


"""
Inicializar un conjunto vacío y agregarle los valores de las siguiente variables
Restricción: Utilizar el metodo add
"""

numero_1 = 1
numero_2 = 2
numero_3 = 3

# COMPLETAR - INICIO
conjunto_1 = set()
conjunto_1.add(numero_1)
conjunto_1.add(numero_2)
conjunto_1.add(numero_3)
# COMPLETAR - FIN

assert conjunto_1 == {1, 2, 3}


"""
Inicializar un conjunto vacío con los valores "5", "6" y "7" y agregarle los valores de
las siguiente variables
Restricción: Utilizar el metodo add
"""

nombre = "Esteban"
domicilio = "Los sauces 3446"
edad = "35"

# COMPLETAR - INICIO
conjunto_2 = {"5","6","7"}
conjunto_2.add(edad)
conjunto_2.add(nombre)
conjunto_2.add(domicilio)
# COMPLETAR - FIN

assert conjunto_2 == {"35", "Esteban", "7", "6", "Los sauces 3446", "5"}


"""
Dados dos conjuntos calcular su interseccion utiilizando el caracter ampersand
"""

conjunto_03 = {1, 23, 4, 8, 5, 10, 15, 21}
conjunto_04 = {12, 4, 10, 21, 78}

# COMPLETAR - INICIO
conjunto_interseccion = conjunto_03 & conjunto_04
# COMPLETAR - FIN

assert conjunto_interseccion == {10, 4, 21}

"""
Dados dos conjuntos calcular su interseccion utiilizando el metodo intersection
"""

conjunto_03 = {1, 23, 4, 8, 5, 10, 15, 21}
conjunto_04 = {12, 4, 10, 21, 78}

# COMPLETAR - INICIO
conjunto_interseccion = conjunto_03.intersection(conjunto_04)
# COMPLETAR - FIN

assert conjunto_interseccion == {10, 4, 21}


"""
Dados dos conjuntos calcular su union utiilizando el caracter pipe
"""

conjunto_05 = {1, 2, 3, 4}
conjunto_06 = {5, 6, 7, 8}

# COMPLETAR - INICIO
conjunto_union = conjunto_05 | conjunto_06
# COMPLETAR - FIN

assert conjunto_union == {1, 2, 3, 4, 5, 6, 7, 8}


"""
Dados dos conjuntos calcular su union utiilizando el metodo union
"""

conjunto_05 = {1, 2, 3, 4}
conjunto_06 = {5, 6, 7, 8}

# COMPLETAR - INICIO
conjunto_union = conjunto_05.union(conjunto_06)
# COMPLETAR - FIN

assert conjunto_union == {1, 2, 3, 4, 5, 6, 7, 8}


"""
Dados dos conjuntos calcular su diferencia utiilizando el caracter menos
"""

conjunto_07 = {1, 2, 3, 4, 5, 6, 7, 8}
conjunto_08 = {2, 4, 6, 8}

# COMPLETAR - INICIO
conjunto_diferencia = conjunto_07 - conjunto_08
# COMPLETAR - FIN

assert conjunto_diferencia == {1, 3, 5, 7}


"""
Dados dos conjuntos calcular su diferencia utiilizando el metodo difference
"""

conjunto_07 = {1, 2, 3, 4, 5, 6, 7, 8}
conjunto_08 = {2, 4, 6, 8}

# COMPLETAR - INICIO
conjunto_diferencia = conjunto_07.difference(conjunto_08)
# COMPLETAR - FIN

assert conjunto_diferencia == {1, 3, 5, 7}


"""
Dados dos conjuntos calcular su diferencia diferencia simetrica utiilizando el caracter circunflejo
"""

conjunto_09 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
conjunto_10 = {1, 2, 3, 5, 6, 7, 8}

# COMPLETAR - INICIO
conjunto_diferencia_simetrica = conjunto_09 ^ conjunto_10
# COMPLETAR - FIN

assert conjunto_diferencia_simetrica == {4, 9}


"""
Dados dos conjuntos calcular su diferencia diferencia simetrica utiilizando el metodo symmetric_difference
"""

conjunto_09 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
conjunto_10 = {1, 2, 3, 5, 6, 7, 8}

# COMPLETAR - INICIO
conjunto_09.symmetric_difference(conjunto_10)
# COMPLETAR - FIN

assert conjunto_diferencia_simetrica == {4, 9}