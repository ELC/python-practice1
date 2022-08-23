"""Coerción a Booleanos"""


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_01
"""

from operator import truth
from pickle import FALSE


A = 5
variable_01=0

# COMPLETAR - INICIO
if ( A == 5):
   variable_01= True

# COMPLETAR - FIN
assert variable_01 is True


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_02
"""

Domicilio = ""

# COMPLETAR - INICIO
if(Domicilio == ""):
    variable_02= False
else:
    variable_02=True    

# COMPLETAR - FIN

assert variable_02 is False


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_03
"""

Domicilio = "Alsina 2446" or "Pueyrredón y la vía"
variable_03 = False

# COMPLETAR - INICIO
if (Domicilio =="Alsina 2446" or Domicilio=="Pueyrredón y la vía"):
    variable_03= True
# COMPLETAR - FIN

assert variable_03 is True


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_04
"""

lista_de_compras = "No comprar nada" and ["Pan", "Aceite", "Sal"]
variable_04=False
# COMPLETAR - INICIO)
if (lista_de_compras == ("No comprar nada" and ["Pan", "Aceite", "Sal"])):
    variable_04=True
# COMPLETAR - FIN

assert variable_04 is True


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_05
"""

lista_de_ids = 0 and [1236, 5565, 8956, 2534]
variable_05= True

# COMPLETAR - INICIO
if (lista_de_ids == (0 and [1236, 5565, 8956, 2534])):
    variable_05=False
# COMPLETAR - FIN

assert variable_05 is False


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_06
"""

diccionario = {} and {"Nombre": "Alberto Paz", "DNI": 12365855}
variable_06=True

# COMPLETAR - INICIO
if (diccionario == ({} and {"Nombre": "Alberto Paz", "DNI": 12365855})):
    variable_06=False
# COMPLETAR - FIN

assert variable_06 is False