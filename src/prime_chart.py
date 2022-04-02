from src.find_primes import prime_implicants


def solve_chart(n_variables, funcion, redundancia):
    primes = prime_implicants(n_variables, funcion, redundancia)
    essential_terms = []

    primes.sort(key=(lambda x: len(x.implicants)))

    i = 0
    while (i < len(funcion)):
        frecuencia = 0
        last = 0
        for a in primes:
            if funcion[i] in a.implicants:
                frecuencia += 1
                last = a

        # print(funcion[i], frecuencia)

        if frecuencia == 1:
            # print(last)
            primes.remove(last)
            essential_terms.append(last)
            for i in last.implicants:
                if i in funcion:
                    funcion.remove(i)
            i = 0
        else:
            i += 1

    print("")
    print("Esenciales: ")
    for i in essential_terms:
        print(i.binary, i.implicants)

    print("")
    print("No Esenciales:", funcion)
    for i in primes:
        print(i.binary, i.implicants)
    print("")
