from src.Utils import Utils


class Input():

    @classmethod
    def integer(cls: type, message="") -> int:
        """ Capturar entero """
        print(message)
        while(True):
            foo = input()
            if foo.isnumeric():
                break
            else:
                print("DATO INVALIDO")
        
        return int(foo)

    @classmethod
    def char(cls: type, message="") -> str:
        """ Capturar caracter """
        print(message)
        return input()[0]

    @classmethod
    def list(cls: type, message="", separator=",") -> list:
        """ Captura una lista de enteros """
        print(message)
        foo = input().split(separator)
        return [ int(e) for e in foo if e.isnumeric() ]

    @classmethod
    def validate(cls: type, n_variables: int, function: list) -> list:
        """ Elimina los valores repetidos y que esten fuera del rango de las variables """
        function = list(set(function))  # eliminar elementos repetidos
        valid_function = []
        max_value = 1 << n_variables

        for i in function:
            if i >= max_value or i < 0:
                print(i, "FUERA DE RANGO")
            else:
                valid_function.append(i)

        return valid_function

    @classmethod
    def from_table(cls: type):
        """ Captura los datos en forma de tabla. { '1' ; Verdadero, '0' : Falso, '-' : Redundancia } """
        m, d = [], []
        n = Input.integer("NUMERO VARIABLES?")

        print("")
        for i in range(0, 1 << n):
            foo = input("".join([
                "%03d" % i,
                " | ",
                Utils.bindigits(i, n),
                "? "
            ]))

            if foo == '-': d.append(i)
            if foo == '1': m.append(i)
            
        return n, m, d

    @classmethod
    def from_list(cls: type):
        """ Capturar los datos en forma de lista, los elementos deben estar separados por ',' """
        n = Input.integer("NUMERO VARIABLES?")
        m = Input.list("ACTIVACION?")
        d = Input.list("REDUNDANCIA?")

        return n, m, d

    @classmethod
    def select(cls: type) -> tuple:
        """ Seleccionar como ingresar los datos al programa """
        while (1):
            e = Input.char("0.LISTA / 1.TABLA?")
            if e == '0':
                return Input.from_list()
            elif e == '1':
                return Input.from_table()
            else:
                print("TIPO INVALIDO")
