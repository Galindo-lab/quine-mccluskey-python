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


def select_input_type() -> tuple:
    """ Seleccionar como ingresar los datos al programa """
    while (1):
        print("0.LISTA / 1.TABLA?")
        e = input()
        if e == '0':
            return Input.from_list()
        elif e == '1':
            return Input.from_table()
        else:
            print("TIPO INVALIDO")


def print_table(m: list) -> None:
    """ Implime los valores de una tabla """
    for i in m:
        print(i.binary, '|', i.implicants)


def x():
    clear_screen()
    print_title()

    n, m, d = select_input_type()

    solve_chart(n, m, d)


#x()
