""""Tuplas y Desempaquetado"""


"""
A partir de ls siguiente lista instanciar una tupla que contenga todos sus valores
y en el mismo orden.
"""

lista = ["casa", "perro", "pato", "gato"]

tupla = tuple(lista)

assert tupla == ("casa", "perro", "pato", "gato")

print (tupla)


"""
A partir de ls siguiente tupla instanciar una lista que contenga todos sus valores
y en el mismo orden.
"""

tupla = "casa", "perro", "pato", "gato", "tenedor"

lista = list(tupla)

assert lista == ["casa", "perro", "pato", "gato", "tenedor"]

print (lista)

"""
Desempaquetar la siguiente tupla en las variables a, b y c
"""

tupla = ("primer", 25, [1, 2, 3])

a,b,c = ("primer",25, [1,2,3])

assert a == "primer" and b == 25 and c == [1, 2, 3]




"""
Desempaquetar la siguiente tupla y luego sumar sus valores
"""

tupla = (87, 98, 35, 67, 4, 9)

a,b,c,d,e,f = (87,98,35,67,4,9)
total = 87 + 98 + 35 + 67 + 4 + 9

assert total == 300

print (total)


"""
Desempaquetar la siguiente lista y luego concatenar sus elementos
Restricción: Utilizar f-Strings.
"""

lista = ["esta", "mañana", "sali", "a", "correr"]

a,b,c,d,e = lista
string_concatenado = f"{a} {b} {c} {d} {e}"

assert string_concatenado == "esta mañana sali a correr"

print (string_concatenado)


"""
Desempaquetar el primer elemento de la siguiente tupla
Restricción: Utilizar desempaquetado con comodines
"""

tupla = (73, 45, 344, 3434, 2)

a, *reset = tupla
primer = a

assert primer == 73

print (primer)


"""
Desempaquetar el primer y el último elemento de la siguiente lista y luego sumarlos
Restricción: Utilizar desempaquetado con comodines
"""

lista = [73, 45, 344, 3434, 2]

a, *reset, b = lista 
suma = a + b
assert suma == 75

print (suma)


"""
Desempaquetar el primer, el segundo, el tercer, el cuarto y el quinto elemento de la
siguiente tupla y luego concatenarlos
Restricción: Utilizar desempaquetado con comodines y f-Strings
"""

tupla = ("anoche", "fui", "a", "la", "fiesta", "pero", "no", "pude", "entrar")

a,b,c,d,e,*rest = tupla
string_concatenado = f'{a} {b} {c} {d} {e}'

assert string_concatenado == "anoche fui a la fiesta"

print (string_concatenado)