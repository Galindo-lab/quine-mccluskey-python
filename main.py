
from math import *
from utils.bindigits import bindigits
from utils.count_set_bits import count_set_bits
from utils.implicants import implicants

def adyasent_terms(a,b):
    # revisar si dos terminos son adyasentes en el mapa de Karnaugh.
    # osea que tienen el mismo valor implicante
    # ejmplo: [0,1] y [8,9] sus implicante son 000- y 100-
    #         por lo tanto son adyasentes.
    return implicants(a) == implicants(b)

def active_implicant_bits(a):
    # numero de bits activos en el mplicante
    # ejemplo: [1,0,8,9] su implicante es -00- por lo tanto
    #          la funcion retornara 0.
    return count_set_bits( (implicants(a) & a[0]) )

# def is_minterm(list_minterm,minterm):
#     for min in list_minterm:
#         if implicants(mint) == 
    


print("Ready...")

# bindigits( (8+9) ^ (0+1) , 8 )
# bindigits( ~((4&6&12&14) + (~4&~6&~12&~14)) ,10)

# Variables ------------------------------------------------------------

# Pruebas

# m = [0,1,8,3,9,7,11,15]         

# solucion: C'D' + BD' + AD' + AB'C' + ABC + A'B'CD
# http://www.32x8.com/sop4_____A-B-C-D_____m_0-3-4-6-8-9-10-12-14-15___________option-1_____989780975078827292690y
m = [0,3,4,6,8,9,10,12,14,15]
# m = [0,1,3,7,8,9,11,15]

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

for a in grupos:
    implicante_primo = True
    for b in grupos:
        if active_implicant_bits(a)+1 == active_implicant_bits(b):                
            if adyasent_terms(a,b):
                print(a+b)

# for i in grupos:
#     for a in implicantes:
#         print(i,a)


# grupos2 = []  

# for a in range(len(grupos)):
#     implicante_primo = True
#     for b in range(a,len(grupos)):
#         if implicants(grupos[b]) == implicants(grupos[a]):
#             if count_set_bits(implicants(grupos[a]) & grupos[a][0])+1 == count_set_bits(implicants(grupos[b]) & grupos[b][0]):
#                 if grupos[b] != grupos[a]:
#                     implicantes.append(grupos[a] + grupos[b])
#                     print(grupos[a] + grupos[b])
#             if count_set_bits( (implicants(grupos[a]) & grupos[a][0]) ^ (implicants(grupos[b]) & grupos[b][0]) ) == 1:
#                 grupos2.append(grupos[a] + grupos[b])


