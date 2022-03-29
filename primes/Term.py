
class Term():

    def __init__(self, implicats, binary):
        self.implicatns = implicants
        self.binary = binary
        self.n_ones = Term.count_ones(binary)

    @classmethod
    def count_ones(cls, a: str) -> int:
        """ Cuenta cuantos '1' aparecen en un string """
        return a.count("1")

    
