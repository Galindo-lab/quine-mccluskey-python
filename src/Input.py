from src.Utils import Utils


class Input():

    @classmethod
    def integer(cls: type, message: str) -> int:
        """ Capturar entero """
        return int(input(message))

    @classmethod
    def char(cls: type, message: str) -> str:
        """ Capturar caracter """
        return input(message)[0]

    @classmethod
    def from_table(cls: type):
        """
        Captura los datos en forma de tabla.
         '1' - Verdadero 
         '0' - Falso
         '-' - Redundancia
        """
        m, d = [], []
        n = Input.integer("Numero de variables: ")

        print("")
        for i in range(0, 1 << n):
            foo = Input.char(" ".join([
                "%3s |" % str(i),
                Utils.bindigits(i, n),
                ": ",
            ]))

            if foo == '-': d.append(i)
            if foo == '1': m.append(i)
        print("")

        return n, m, d

    @classmethod
    def from_list(cls: type):
        """
        Capturar los datos en forma de lista, los elementos deben estar separados por ','
        """
        n = Input.integer("Numero de variables: ")
        print("Activacion: ")
        m = input().split(",")
        print("Redundancia: ")
        d = input().split(",")
        return n, m, d
