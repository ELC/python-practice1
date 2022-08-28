"""Conversiones Básicas"""


"""
Convertir los numeros de string a enteros y luego sumarlos.
"""

numero_01 = "123"
numero_02 = "456"
numero_03 = "789"
numero_04 = "132"

suma_de_numeros=int(numero_01)+int(numero_02)+int(numero_03)+int(numero_04)

assert suma_de_numeros == 1500

print (suma_de_numeros)


"""
Convertir los numeros de enteros a string y luego concatenarlos.
"""

numero_01 = 123
numero_02 = 456
numero_03 = 789

suma_de_numeros_string=str(numero_01)+ str(numero_02)+ str(numero_03)

assert suma_de_numeros_string == "123456789"

print (suma_de_numeros_string)


"""
Convertir los numeros de binario, octal y hexadecimal a enteros y luego
multiplicarlos.
"""

numero_binario = "0b111010110101110111101000000"
numero_octal = "0o1425"
numero_hexadecimal = "0x6f540"

multiplicacion_de_numeros=int(numero_binario,2)*int(numero_octal,8)*int(numero_hexadecimal,16)

assert multiplicacion_de_numeros == 44397345600000000

print (multiplicacion_de_numeros)


"""
Convertir todo los numeros a enteros y luego restarlos secuencialmente (El uno
menos el dos menos el tres menos el cuatro).
"""

numero_01 = "987"
numero_02 = "0x6f54F"
numero_03 = "0o1234"
numero_04 = 654

resultado_resta=int(numero_01)-int(numero_02,16)-int(numero_03,8)-numero_04

assert resultado_resta == -456350

print (resultado_resta)