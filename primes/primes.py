from Term import Term

import timeit
import time

print("Ready ...")

# solucion particular: shorturl.at/uBX19

# variables de la funcion
# TODO: Convertirlo en una lista para que el usuario pueda nombrar sus variables.
n_variables = 4

# normalmente llamada 'm', valores de interes
funcion = [1, 4, 8, 10, 11, 12, 15]

# valores que son indiferetes, normalemnte llamados 'd'
redundacia = [14]

def sort_by_ones(m: list) -> list:
    m.sort(key=(lambda x: x.n_ones))

def print_table(m: list) -> None:
    for i in m: print(i)
    
def create_table(n, m, d):
    tbl = []
    # funcion mas redundacia
    terminos = m + d
    for value in terminos:
        tbl.append(Term.from_int(value, n))
    sort_by_ones(tbl)
    return tbl
    

def extract_prime_terms(m: list) -> list:
    """ este es un metodo destructivo """
    tbl_size = len(m)
    primes = []
    i = 0
    for a in m:
        is_prime = True
        for b in m:
            if Term.diference(a, b) == 1:
                is_prime = False
                break
        if is_prime:
            primes.append(a)
        else:
            continue

    for i in primes:
        m.remove(i)
        
    return primes

def tabulate(m: list) -> list:
    tbl_size,foo,i = len(m),[],0

    while( i < tbl_size ):
        for j in range(i, tbl_size):
            if m[i].n_ones+1 < m[j].n_ones:
                break
            
            if Term.diference(m[i],m[j]) == 1:
                foo.append( Term.combine(m[i],m[j]) )
        i += 1
        
    return foo
        
    
def test():
    start_time = timeit.default_timer()
    n_variables = 4
    # normalmente llamada 'm', valores de interes
    funcion = [0, 2, 5, 7, 8, 10, 13, 15]
    # valores que son indiferetes, normalemnte llamados 'd'
    redundacia = []

    
    primes = []
    d = create_table(n_variables, funcion, redundacia)
    primes += extract_prime_terms(d)
    
    while(len(d) != 0):    
        print("")
        print("TABLE " + "-"*10)
        print_table(d)
        print("PRIMES " + "-"*10)
        print_table(primes)
        d = tabulate(d)
        primes += extract_prime_terms(d)
        sort_by_ones(d)

    print("")
    print("TABLE " + "-"*10)
    print_table(d)
    print("PRIMES " + "-"*10)
    print_table(primes)
    print(timeit.default_timer() - start_time)

