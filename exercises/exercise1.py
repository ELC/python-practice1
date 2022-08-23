"""Aritmética Básica"""


"""
Calcular el área del cuadrado usando las variables disponibles.
Restricción: Usar el operador de multiplicación
"""

lado_cuadrado = 5

# COMPLETAR - INICIO
area_cuadrado=lado_cuadrado * lado_cuadrado
# COMPLETAR - FIN
print("El area del cuadrado es: " , area_cuadrado )

assert area_cuadrado == 25


"""
Re-Escribir usando el operador de potencia.
"""

lado_cuadrado = 5

# COMPLETAR - INICIO
area_cuadrado = lado_cuadrado ** 2 
# COMPLETAR - FIN

assert area_cuadrado == 25


"""
Re-Escribir usando la función pow.
"""

lado_cuadrado = 5

# COMPLETAR - INICIO
print("El area es: " ,pow(lado_cuadrado,2))
# COMPLETAR - FIN

assert area_cuadrado == 25



"""
Calcular la cantidad de unidades a comprar.
Restricción: Usar el operador de división entera.
"""

precio = 3.74
presupuesto_disponible = 10

# COMPLETAR - INICIO
cantidad_a_comprar = presupuesto_disponible//precio
# COMPLETAR - FIN
print("Cantidad a comprar: ", cantidad_a_comprar)

assert cantidad_a_comprar == 2


"""
Determinar si el número de la variable es divisible por 7.
Restricción: Usar el operador módulo.
"""

numero_incalculable = 2 ** 54 - 1

# COMPLETAR - INICIO
es_divisible_por_siete = numero_incalculable % 7
# COMPLETAR - FIN
print( es_divisible_por_siete)

assert es_divisible_por_siete

