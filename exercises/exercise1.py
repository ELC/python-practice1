"""Aritmética Básica"""


"""
Calcular el área del cuadrado usando las variables disponibles.
Restricción: Usar el operador de multiplicación
"""

lado_cuadrado = 5

area_cuadrado = lado_cuadrado * lado_cuadrado

assert area_cuadrado == 25

print ("El area al cuadrado es:")
print (area_cuadrado)

"""
Re-Escribir usando el operador de potencia.
"""

lado_cuadrado = 5

area_cuadrado = lado_cuadrado**2
assert area_cuadrado == 25

print ("El area al cuadrado es:")
print (area_cuadrado)




"""
Re-Escribir usando la función pow.
"""

lado_cuadrado = 5

area_cuadrado = pow(5,2)
assert area_cuadrado == 25

print ("El area al cuadrado es:")
print (area_cuadrado)



"""
Calcular la cantidad de unidades a comprar.
Restricción: Usar el operador de división entera.
"""

precio = 3.74
presupuesto_disponible = 10

cantidad_a_comprar= presupuesto_disponible // precio

assert cantidad_a_comprar == 2
print("La cantidad a comprar es: ")
print(cantidad_a_comprar)

"""
Determinar si el número de la variable es divisible por 7.
Restricción: Usar el operador módulo.
"""

numero_incalculable = 2 ** 54 - 1

es_divisible_por_siete = numero_incalculable % 7

assert es_divisible_por_siete == 0
print("El numero es divisible")