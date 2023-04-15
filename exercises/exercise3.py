"""Comparación"""

"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si 2 personas tienen el mismo nombre pero distinta edad.
Aclaración: Se puede utilizar and, or y not.
"""

persona_01 = "Kevin"
edad_01 = 24
persona_02 = "Kevin"
edad_02 = 41

# COMPLETAR - INICIO
comparar_nombre_y_edad = (persona_01 == persona_02) and (edad_01 != edad_02)
# COMPLETAR - FIN
print(comparar_nombre_y_edad)
assert comparar_nombre_y_edad


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si un auto no es de marca Ford y su modelo es igual o anterior al año 2000.
Aclaración: Se puede utilizar and, or y not.
"""

marca_del_auto = "Chevrolet"
modelo_de_auto = 1998

# COMPLETAR - INICIO
comparar_marca_y_modelo =(marca_del_auto != "Ford") and (modelo_de_auto <= 2000)
# COMPLETAR - FIN
print(comparar_marca_y_modelo)
assert comparar_marca_y_modelo


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si la superfice del campo 1 es menor a la del campo 2 y la superficie del
campo 2 es mayor a la del campo 3.
Restricción: Utilizar comparaciones encadenadas - No utilizar and, or ni not.
"""

superficie_de_campo_01 = 85121
superficie_de_campo_02 = 851212
superficie_de_campo_03 = 8512

# COMPLETAR - INICIO
comparar_superficie = superficie_de_campo_01 < superficie_de_campo_02 > superficie_de_campo_03
# COMPLETAR - FIN
print(comparar_superficie)
assert comparar_superficie


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si la cantidad de bananas es menor a la mitad de la cantidad de naranjas,
la mitad de naranjas es menor a dos veces la cantidad de manzanas y dos veces
la cantidad de manzanas es menor o igual a la cantidad de peras al cuadrado.
Restricción: Utilizar comparaciones encadenadas y no utilizar and, or ni not.
"""

bananas = 100
naranjas = 400
manzanas = 300
peras = 30

# COMPLETAR - INICIO
comparar_frutas = bananas < (naranjas/2) < (manzanas * 2) <= (peras**2)
# COMPLETAR - FIN
print(comparar_frutas)

assert comparar_frutas