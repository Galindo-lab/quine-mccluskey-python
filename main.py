
from math import *
from utils.bindigits import bindigits
from utils.count_set_bits import count_set_bits

print("Ready...")

# bindigits( (8+9) ^ (0+1) , 8 )
# bindigits( ~((4&6&12&14) + (~4&~6&~12&~14)) ,10)

# Variables ------------------------------------------------------------

# Pruebas

# solucion: C'D' + BD' + AD' + AB'C' + ABC + A'B'CD
# http://www.32x8.com/sop4_____A-B-C-D_____m_0-3-4-6-8-9-10-12-14-15___________option-1_____989780975078827292690y
m = [0,2,3,4,6,8,9,10,12,14,15]

# funcion 1
# m = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# funcion 0
# m = []                         

n = 4                           # numero de variables


# Procedimiento --------------------------------------------------------
m.sort(key=count_set_bits)      # ordenar por numero de 1


# la maxima simplificacion 
# fuente: https://es.wikipedia.org/wiki/Mapa_de_Karnaugh
reducciones_maximas = int(sqrt(2**n))

grupos = []            # grupos que continuan a la siguiente iteracion
implicantes = []       # implicantes que ya no pueden ser reducidos

for a in range(len(m)):
    implicante_primo = True
    for b in range(a,len(m)):   # evitamos evaluar 2 veces los elementos

        # no vale la pena seguir iterando cuando en numero de bits difetente
        # es mayor a 1.
        if count_set_bits(m[b]) > count_set_bits(m[a])+1:
            if implicante_primo:
                # no puede ser agrupado con otros terminos por lo tanto
                # NO puede ser simplificado
                implicantes.append( [m[a]] )
            break 
        
        if count_set_bits(m[a]^m[b]) == 1: # numero de bits diferentes
            grupos.append( [m[a],m[b]] )
            # Esto significa que el termino no sirve para la tabla de
            # implicantes primos porque todavia puede ser simplificado
            implicante_primo = False 

# NOTE: los implicantes obtenidos son 'parciales', 

            
print("grupos: ",grupos)
print("implicantes: ",implicantes)


