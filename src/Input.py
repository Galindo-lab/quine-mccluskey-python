from src.Utils import Utils


class Input():

    @classmethod
    def integer(cls: type, message="") -> int:
        """ Capturar entero """
        return int(input(message))

    @classmethod
    def char(cls: type, message="") -> str:
        """ Capturar caracter """
        return input(message)[0]

    @classmethod
    def list(cls: type, message="", separator=",", Type=str) -> list:
        """ Captura una lista """
        return list(map(Type, input(message).split(separator)))

    @classmethod
    def validate(cls: type, n_variables: int, function: list) -> list:
        """ Elimina los valores repetidos y que esten fuera del rango de las variables """
        function = list(set(function))  # eliminar elementos repetidos
        valid_function = []
        max_value = 1 << n_variables

        for i in function:
            if i >= max_value or i < 0:
                print(i, "fuera de rango")
            else:
                valid_function.append(i)

        return valid_function

    @classmethod
    def from_table(cls: type):
        """ Captura los datos en forma de tabla. { '1' ; Verdadero, '0' : Falso, '-' : Redundancia } """
        m, d = [], []
        n = Input.integer("Numero vars: ")

        print("")
        for i in range(0, 1 << n):
            foo = Input.char(" ".join([
                "%3s |" % str(i),
                Utils.bindigits(i, n),
                ": ",
            ]))

            if foo == '-': d.append(i)
            if foo == '1': m.append(i)

        m = Input.validate(n, m)
        d = Input.validate(n, d)

        return n, m, d

    @classmethod
    def from_list(cls: type):
        """ Capturar los datos en forma de lista, los elementos deben estar separados por ',' """
        n = Input.integer("Numero vars: ")
        print("Activacion: ")
        m = Input.list(Type=int)
        print("Redundancia: ")
        d = Input.list(Type=int)

        m = Input.validate(n, m)
        d = Input.validate(n, d)

        return n, m, d
