from src.count_set_bits import count_set_bits
from src.bindigits import bindigits
from src.combine_implicants import combine_implicants
from src.count_ones import count_ones
from src.difference import difference

# Functions --------------------------------------------------

IMPLICANTS = 0


def implicants_table(m: list, d: list, n: int) -> list:
    """Crea la tabla de implicantes de primer orden

    Parameters
    ----------
    m : list
        Valores de interes para la funcion
    d : list
        Valores indiferentes
    n : int 
        Numero de variables

    Returns
    -------
    list
        Tabla de valores con su represetacion binaria
    """
    f = m + d
    f.sort(key=count_set_bits)
    table = [[[e], bindigits(e, n)] for e in f]
    return table


def combine_term(a: list, b: list) -> list:
    """une dos terminos de tabla de implicantes

    Parameters
    ----------
    a : list
        Termino 'a'
    d : list
        Termino 'b'

    Returns
    -------
    list
        Union de 'a' con 'b'
    """
    foo = a[0] + b[0]
    foo.sort()
    implicants = combine_implicants(a[1], b[1])
    return [foo, implicants]


def sort_by_ones(m: list) -> list:
    s = lambda x: count_ones(x[1])
    m.sort(key=s)


def remove_primes(table: list, primes: list):
    for p in primes:
        table.remove(p)


def find_primes(m: list) -> list:
    primes = []
    for a in m:
        is_prime = True
        for b in m:
            if difference(a[1], b[1]) == 1:
                is_prime = False
                break
        if is_prime:
            primes.append(a)
        else:
            continue
    return primes


def tabulate(m):
    table = []
    for a in m:
        for b in m:
            if a != b and difference(a[1],b[1]) == 1:
                c = combine_term(a,b)
                if c not in table:
                    table.append(c)
    m.clear()
    for i in table:
        m.append(i)        



def find_implicants():
    # numero de variables
    n = 4
    
    # valores de activacion
    m = [4, 8, 10, 11, 12, 15, ]
    
    # valores indiferentes
    d = [9, 14]

    table = implicants_table(m, d, n)
    primes = []
    
    while(len(table) != 0):
        foo = find_primes(table)
        primes += foo
        remove_primes(table,foo)
        tabulate(table)

    return primes
