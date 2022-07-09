def unos(numero: int) -> int:
    """
    numero de unos en la representacion binaria
    """
    return bin(numero).count("1")


def diferencias(a: str, b: str) -> int:
    """
    numero de caracteres diferentes en un string 
    del mismo tamaño
    """
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]: count += 1
    return count


def bindigits(number: int, digits: int) -> str:
    """
    Convertir numero a binario de tamaño fijo
    """
    return "{0:0{1}b}".format(number, digits)


class Termino:
    """
    Esta clase unifica la lista de implicantes 
    con su representación, es un fila de la tabla
    de implicantes primos.
    """
    representacion: str
    implicantes: tuple
    variables: int  # numero variables

    # esencial:bool

    def __init__(self, variables: int, implicantes: tuple):
        self.implicantes = implicantes
        self.variables = variables
        self.representacion = ""
        # self.esencial = False

    def __str__(self):
        foo = self.representacion + " " + str(self.implicantes)
        return foo

    def regenerar(self):
        """
        Regenera la representacion del implicante
        """
        output = [None] * self.variables  # output
        # base
        b = bindigits(self.implicantes[0], self.variables)

        for implicante in self.implicantes:
            # termino
            a = bindigits(implicante, self.variables)

            for i in range(len(a)):
                output[i] = '-' if a[i] != b[i] else b[i]

        self.representacion = "".join(output)

    def es_adyacente(self, b):
        return diferencias(self.representacion, b.representacion) == 1

    def combine(self, a):
        # elimina los valore repetidos y
        # une las dos tuplas de implicantes
        implicantes = tuple(set(self.implicantes + a.implicantes))
        variables = self.variables
        return Termino.por_minterminos(variables, implicantes)

    @classmethod
    def por_minterminos(cls, variables, implicantes):
        foo = Termino(variables, implicantes)
        foo.regenerar()
        return foo


# *********************************************************
#                          CODE
# *********************************************************


def extraer_primos(nvariables, terminos):
    a = []  # iteracion actual
    b = []  # siguiente iteracion
    primos = []  # lista de terminos de implicantes primos
    existentes = []  # lista de representaciones de los implicantes

    for termino in terminos:
        a.append(Termino.por_minterminos(nvariables, [termino]))

    while len(a) != 0:
        for i in a:
            cnv = 0
            for j in a:
                if not i.es_adyacente(j): continue

                cnv += 1
                termino = i.combine(j)

                if not (termino.representacion in existentes):
                    b.append(termino)
                    existentes.append(termino.representacion)

            if cnv == 0:
                primos.append(i)

        a = b.copy()
        b = []

    return primos


def esenciales(primos, minter):
    indice_esenciales = []
    foo = []

    for i in minter:
        freq = 0
        term = None
        for count, j in enumerate(primos):
            if not i in j.implicantes: continue
            if freq == 1:
                term = None
                break
            freq += 1
            term = count

        if term != None:
            # primos[term].esencial = True
            indice_esenciales.append(term)

    for i in indice_esenciales:
        foo.append(primos[i])
        primos[i] = None

    i = 0  # remove nones
    while True:
        if i >= len(primos): break
        if primos[i] == None:
            primos.pop(i)
        else:
            i += 1

    return foo


print("")

nvariables = 4

minterminos = [4, 8, 10, 11, 12, 15]
redundancias = [9, 14]

# minterminos = [2,7,9,10,11,15]
# redundancias = [1,8]

# minterminos = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# redundancias = []

todos_los_terminos = minterminos + redundancias

primos = extraer_primos(nvariables, todos_los_terminos)
terminos_esenciales = esenciales(primos, minterminos)

print("*** Esenciales ***")
for i in terminos_esenciales:
    print(i)

print("")

print("*** No Esenciales ***")
for i in primos:
    print(i)
