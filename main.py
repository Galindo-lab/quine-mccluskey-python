
from primes.find_primes import prime_implicants
from primes.prime_chart import solve_chart

def print_table(m: list) -> None:
    """ Implime los valores de una tabla  """
    for i in m:
        print(i.binary, '|', i.implicants)

def capture_function(n_variables):
    """  """
    funcion, redundancia = [], []
    for i in range(0,1<<n_variables):
        captura = input(str(i)+ ": ")
        if captura == '1':
            funcion.append(i)
        elif captura == '-':
            redundancia.append(i)
    return funcion, redundancia
            
def x():
    n = int(input("Numero de variables: "))
    m, d = capture_function(n)

    # n = 4
    # m = [4,8,10,11,12,15]
    # d = [9,14]

    # n = 4
    # m = [0,1,11,13,15]
    # d = []
    
    # print("Tabla" + (10 * '-'))
    solve_chart(n,m,d)
    # print_table(prime_implicants(n, m, d))

x()


