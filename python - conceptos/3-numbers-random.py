####################### --- NUMBERS ---
# int integer: número entero
numero_entero = 1

# float: numero decimal
numero_decimal = 3.14

# complex: numero complejo (parte entera y otra parte imaginaria)
numero_complejo = 5 + 2j

# print(type(numero_entero))
# print(type(numero_decimal))
# print(type(numero_complejo))

####################### --- CASTEO ---

decimal_desde_entero = float(numero_entero)
entero_desde_entero = int(numero_decimal)
complejo_desde_entero = complex(numero_entero)
complejo_desde_decimal = complex(numero_decimal)
# entero desde complejo no se puede transformar

# print(decimal_desde_entero)
# print(entero_desde_entero)
# print(complejo_desde_entero)
# print(complejo_desde_decimal)

####################### --- RANDOM ---

import random

aleatorio = random.randrange(1, 10)  # el numero de stop no es incluyente

aleatorio_par = random.randrange(2, 11, 2)  # numero par del 2 al 10 incluido

aleatorio_impar = random.randrange(1, 10, 2)  # numero impar del 1 al 9 incluido
