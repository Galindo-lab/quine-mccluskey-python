class Utils():

    @classmethod
    def bindigits(cls: type, number: int, digits: int) -> str:
        """ Convertir numero a binario de tamaño fijo """
        return "{0:0{1}b}".format(number, digits)

    @classmethod
    def intlen(cls: type, number: int) -> int:
        """ Longitud de un numero """
        return len(str(number))
