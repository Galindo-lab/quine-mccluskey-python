from src.find_primes import prime_implicants
from src.prime_chart import solve_chart

from src.Input import Input


def clear_screen() -> None:
    """ Dejar la pantalla lo mas limpia posible """
    print("\n" * 7)


def print_title() -> None:
    """ Imprime el titulo del programa """
    print("\n".join([
        "---------------------",
        "      REDUCCION      ",
        "  DE FUNCION LOGICA  ",
        "---------------------\n",
    ]))


def print_table(m: list) -> None:
    """ Implime los valores de una tabla """
    for i in m:
        print(i.binary, '|', i.implicants)


def x():
    clear_screen()
    print_title()

    n, m, d = Input.select()

    print("\n------ RESULTS ------\n")
    print("LOGS:")
    m = Input.validate(n,m)
    d = Input.validate(n,d)
    print("")

    solve_chart(n, m, d)

x()
