
from src.find_primes import prime_implicants
from src.prime_chart import solve_chart

from src.Input import Input

def print_table(m: list) -> None:
    """ Implime los valores de una tabla  """
    for i in m:
        print(i.binary, '|', i.implicants)
            
def x():
    # n,m,d = Input.from_table()
    n,m,d = Input.from_list()

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


