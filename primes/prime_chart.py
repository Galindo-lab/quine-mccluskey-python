
from primes.find_primes import prime_implicants

def solve_chart(n_variables, funcion, redundancia):
    primes = prime_implicants(n_variables, funcion, redundancia)
    essential_terms = []


    i = 0
    while(i < len(funcion)):
        frecuencia = 0
        for a in primes:
            if funcion[i] in a.implicants :
                essential = a
                frecuencia += 1
            elif frecuencia > 1:
                continue

        if frecuencia == 1:
            essential_terms.append(essential)
            primes.remove(essential)
            for a in essential.implicants:
                if a in funcion:
                    funcion.remove(a)
        else:
            i += 1

    
    print(funcion)
    print("Esenciales: ")
    for i in essential_terms:
        print(i)
    print("No esenciales: ")
    for i in primes:
        print(i)


    i = 0
    while(i < len(funcion)):
        frecuencia = 0
        
        
    
    # for i in funcion:
    #     frecuencia = 0
    #     for a in primes:
    #         if frecuencia == 0 and i in a.implicants :
    #             essential = a
    #             frecuencia += 1
    #         elif frecuencia > 1:
    #             continue

    #     if frecuencia == 1:
    #         essential_terms.append(essential)
    #         primes.remove(essential)

    print(funcion)
    print("Esenciales: ")
    for i in essential_terms:
        print(i)
    print("No esenciales: ")
    for i in primes:
        print(i)

        
