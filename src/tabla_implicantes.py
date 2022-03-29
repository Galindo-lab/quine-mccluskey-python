
def essential_terms(m,primes):
    essential = []
    for a in m:
        frecuencia = 0
        foo = []
        for b in primes:
            if a in b[0]:
                frecuencia += 1
                foo = b
                if frecuencia > 1:
                    break
        if frecuencia == 1:
            m.remove(a)
            essential.append(foo)
    return essential
                
def remove_terms(a,b):
    for i in b:
        a.remove(i)

            
def prime_implicants(m,primes):
    print("a")
    essential = []
    e = []
    primes_copy = [x for x in primes]
    
    while( len(primes_copy) > 1 ):
        e = essential_terms(m,primes_copy)
        essential += e
        print(e)
        remove_terms(primes_copy,e)
        print(len(primes_copy))

    return essential

    
