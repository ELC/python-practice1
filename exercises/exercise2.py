"""Lógica Simple y Cortocircuito"""


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si al menos una de las variables es True.
"""

from asyncore import read
from operator import truediv
from webbrowser import get


esta_lloviendo = True
riego_activado = True

piso_mojado = (esta_lloviendo) or (riego_activado)


assert piso_mojado

print (piso_mojado)


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el área es mayor a 5.
Restricción: Usar NOT.
"""

lado_cuadrado = 5
area_cuadrado = pow(lado_cuadrado, 2)

area_mayor_a_cinco = area_cuadrado and not(area_cuadrado < 5)


assert area_mayor_a_cinco

print(area_mayor_a_cinco)

"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el número 1 es divisible por 7 y al mismo tiempo el número 2 no lo es.
"""

numero_1 = 49
numero_2 = 50

resultado = ((numero_1 % 7 == 0)    and (numero_2  % 7 != 0))

assert resultado

print (resultado)


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
el mismo valor de la variable 3.
Restricción: sólo usar OR, NOT y el mecanismo de cortocircuito.
"""

variable_01 = False
variable_02 = True
variable_03 = 80
variable_04 = 90
variable_05 = 100

resultado = variable_03 or variable_02 or not variable_01 or not variable_04 or not variable_05

assert resultado == 80

print (resultado)