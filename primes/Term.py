
class Term():

    def __init__(self, implicatns, binary):
        self.implicatns = implicatns
        self.binary = binary
        self.n_ones = Term.count_ones(binary)


    @classmethod
    def from_int(cls: type, number: int, n_variables: int) -> type:
        return cls([value], Term.bindigits(number, n_variables))

    @classmethod
    def bindigits(cls: type, number: int,digits: int) -> str:
        """ Convertir numero a binario de tamaño fijo """
        return "{0:0{1}b}".format(number,digits)

        
    @classmethod
    def count_ones(cls, a: str) -> int:
        """ Cuenta cuantos '1' aparecen en un string """
        return a.count("1")

    
