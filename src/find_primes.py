from src.Term import Term


def create_table(n: int, m: list, d: list):
    """ Crea las primesras tablas de minterminos """
    tbl = []
    terminos = m + d  # funcion mas redundancia
    for value in terminos:
        tbl.append(Term.from_int(value, n))
    tbl.sort(key=(lambda x: x.n_ones))
    return tbl


def is_prime(value: type, table: list) -> bool:
    """ Saber si un valor es primo """
    for element in set(table):
        if Term.diference(value, element) == 1: return False

    return True


def extract_prime_terms(m: list) -> list:
    """ Este es un método destructivo, extrae todos los valores primos de la función """
    alredy = set()
    primes = []
    for a in set(m):
        if is_prime(a, m):
            if a.binary not in alredy:
                primes.append(a)
                alredy.add(a.binary)
    for i in primes:
        m.remove(i)
    return primes


def combinable(a, b):
    """ Revisar que dos valores tengan solo un solo valor de diferencia """
    return a.n_ones > b.n_ones and Term.diference(a, b) == 1


def tabulate(m: list) -> list:
    """ Este es un metodo destructivo, Iterar los valores para formar las combinaciones entre los grupos """
    alredy = set()
    primes = []
    for a in set(m):
        for b in set(m):
            if combinable(a, b):
                c = Term.combine(a, b)
                if c.binary not in alredy:
                    primes.append(c)
                    alredy.add(c.binary)
    m.clear()
    for i in primes:
        m.append(i)

        
def true_function(m,n):
    """ Revisar si todos los elementos estan contenidos en la funcion """
    return len(m) == (1<<n)


def false_function(m):
    """ Reviar si la lista de la funcion esta vacia """
    return len(m) == 0


def prime_implicants(n_variables, funcion, redundancia):
    """ Extraer los implicantes primos de la función """
        
    primes = []
    d = create_table(n_variables, funcion, redundancia)
    primes += extract_prime_terms(d)

    while (len(d) != 0):
        tabulate(d)
        primes += extract_prime_terms(d)

    return primes
