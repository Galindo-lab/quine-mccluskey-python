from Term import Term


def print_table(m: list) -> None:
    for i in m:
        print(i)


def create_table(n, m, d):
    tbl = []
    # funcion mas redundacia
    terminos = m + d
    for value in terminos:
        tbl.append(Term.from_int(value, n))
    tbl.sort(key=(lambda x: x.n_ones))
    return tbl


def is_prime(value, table):

    for element in set(table):
        if Term.diference(value, element) == 1: return False

    return True


def extract_prime_terms(m: list) -> list:
    """ este es un metodo destructivo """
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
    return a.n_ones > b.n_ones and Term.diference(a, b) == 1


def tabulate(m: list) -> list:
    alredy = set()
    primes = []
    for a in set(m):
        for b in set(m):
            if combinable(a, b):
                c = Term.combine(a, b)
                if c.binary not in alredy:
                    primes.append(c)
                    alredy.add(c.binary)
    return primes


def prime_implicants(n_variables, funcion, redundancia):
    primes = []

    d = create_table(n_variables, funcion, redundancia)
    primes += extract_prime_terms(d)

    while (len(d) != 0):
        d = tabulate(d)
        primes += extract_prime_terms(d)
    return primes

