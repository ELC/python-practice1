"""Conversiones Básicas"""


"""
Convertir los numeros de string a enteros y luego sumarlos.
"""

numero_01 = "123"
numero_02 = "456"
numero_03 = "789"
numero_04 = "132"

# COMPLETAR - INICIO
variable_01 = int(numero_01)
variable_02 = int(numero_02)
variable_03 = int(numero_03)
variable_04 = int(numero_04)

suma_de_numeros = variable_01 + variable_02 + variable_03 + variable_04 

# COMPLETAR - FIN
print(f"La suma de los numeros es: {suma_de_numeros}")
assert suma_de_numeros == 1500


"""
Convertir los numeros de enteros a string y luego concatenarlos.
"""

numero_01 = 123
numero_02 = 456
numero_03 = 789

# COMPLETAR - INICIO
variable_01 = str(numero_01)
variable_02 = str(numero_02)
variable_03 = str(numero_03)

suma_de_numeros_string = variable_01 + variable_02 + variable_03 

# COMPLETAR - FIN
print(f"Los numeros concatenados son: {suma_de_numeros_string}")
assert suma_de_numeros_string == "123456789"


"""
Convertir los numeros de binario, octal y hexadecimal a enteros y luego
multiplicarlos.
"""

numero_binario = "0b111010110101110111101000000"
numero_octal = "0o1425"
numero_hexadecimal = "0x6f540"

# COMPLETAR - INICIO
numero_binario = int("0b111010110101110111101000000", 2)
numero_octal = int("0o1425", 8)
numero_hexadecimal = int("0x6f540", 16)

multiplicacion_de_numeros = numero_binario * numero_octal * numero_hexadecimal
# COMPLETAR - FIN
print(f"La multiplicacion es de: {multiplicacion_de_numeros}")

assert multiplicacion_de_numeros == 44397345600000000


"""
Convertir todo los numeros a enteros y luego restarlos secuencialmente (El uno
menos el dos menos el tres menos el cuatro).
"""

numero_01 = "987"
numero_02 = "0x6f54F"
numero_03 = "0o1234"
numero_04 = 654

# COMPLETAR - INICIO
numero_01 = int("987")
numero_02 = int("0x6f54F", 16)
numero_03 = int("0o1234", 8)

resultado_resta = numero_01 - numero_02 - numero_03 - numero_04

# COMPLETAR - FIN
print(f"El resultado es de: {resultado_resta}")
assert resultado_resta == -456350