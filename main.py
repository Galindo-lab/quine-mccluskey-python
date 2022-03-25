
from math import *
from utils.bindigits import bindigits
from utils.count_set_bits import count_set_bits

print("Ready...")

# Variables ------------------------------------------------------------

m = [0,1,3,7,8,9,11,15]         # valores de interés
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
                implicantes.append( (m[a]) )
            continue 
        
        if count_set_bits(m[a]^m[b]) == 1: # numero de bits diferentes
            grupos.append( (m[a],m[b]) )
            # Esto significa que el termino no sirve para la tabla de
            # implicantes primos porque todavia puede ser simplificado
            implicante_primo = False 
            

print("grupos: ",grupos)
print("implicantes",implicantes)
