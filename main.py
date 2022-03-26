
from math import *
from utils.bindigits import bindigits
from utils.count_set_bits import count_set_bits
from utils.implicants import implicants

def same_implicant(a,b):
    return implicants(a) == implicants(b)

def active_implicant_bits(a):
    # numero de bits activos en el mplicante
    # ejemplo: [1,0,8,9] su implicante es -00- por lo tanto
    #          la funcion retornara 0.
    return count_set_bits( (implicants(a) & a[0]) )

def adyasent_terms(a,b):
    return count_set_bits( (implicants(a) & a[0]) ^ (implicants(b) & b[0])  ) == 1


print("Ready...")

# bindigits( (8+9) ^ (0+1) , 8 )
# bindigits( ~((4&6&12&14) + (~4&~6&~12&~14)) ,10)

# Variables ------------------------------------------------------------

# Pruebas

 # m = [0,1,8,3,9,7,11,15]         

# solucion: C'D' + BD' + AD' + AB'C' + ABC + A'B'CD
# http://www.32x8.com/sop4_____A-B-C-D_____m_0-3-4-6-8-9-10-12-14-15___________option-1_____989780975078827292690y
# m = [0,3,4,6,8,9,10,12,14,15]
# m = [0,1,3,7,8,9,11,15]

# funcion 1
# m = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# funcion 0
# m = []                         

# m = [0,7,13]



# m = [0,1,3,7,8,9,11,15]
m = [1,3,4,5,9,11,12,13,14,15]
n = 4                           # numero de variables


# Procedimiento --------------------------------------------------------
m.sort(key=count_set_bits)      # ordenar por numero de 1
m = [[a] for a in m]

# la maxima simplificacion 
# fuente: https://es.wikipedia.org/wiki/Mapa_de_Karnaugh
reducciones_maximas = int(sqrt(2**n))

grupos = []            # grupos que continuan a la siguiente iteracion
implicantes = []       # implicantes que ya no pueden ser reducidos


def find_primes(m):
    # m = [ [i] for i in m ]
    primes = []
    for a in range(len(m)):
        implicante_primo = True
        for b in range(len(m)):
            if adyasent_terms( m[a],m[b] ) and same_implicant(m[a],m[b]) :
                implicante_primo = False
                break
        if implicante_primo:
            primes.append(m[a])
    return primes


def convine_elements(m):
    terms = []
    for a in m:
        for b in m:
            if active_implicant_bits(a)+1 == active_implicant_bits(b):            
                if same_implicant(a,b) and adyasent_terms(a,b) :
                    terms.append(a+b)
    return terms
    

def remove_primes(lista,elements):
    for i in elements:
        lista.remove(i)

def x(m):
    m.sort(key=count_set_bits)      # ordenar por numero de 1
    m = [[a] for a in m]
    primes = []
    while(True):
        primes += find_primes(m)
        remove_primes(m,find_primes(m))
        m = convine_elements(m)
        if len(m) == 0:
            break;
    return primes

