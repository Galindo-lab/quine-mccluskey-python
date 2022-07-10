
def remove_nones(a: list):
    """
    Eliminar todos los elementos 'None' de una lista

    NOTE: Este es un método destructivo, no retorna nada
          pero  si modifica el contenido de la lista.

    """
    i = 0 
    while True:
        if i >= len(a): break
        if a[i] == None:
            a.pop(i)
        else:
            i += 1


def diferencias(a: str, b: str) -> int:
    """
    Numero de caracteres diferentes en un string 
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


# *********************************************************
#                       Clases
# *********************************************************


class Termino:
    """
    Esta clase unifica la lista de implicantes 
    con su representación, es un fila de la tabla
    de implicantes primos.

    Attributes
    ----------
    implicantes : tuple
        lista de minterminos que representa el termino

    representacion : str
        miniterminos en forma de string, cada carácter
        corresponde a una variable, si el valor es '0'
        la variable esta negada, si es '-' es que no
        se usa esa variable para representar los 
        implicantes

    variables : int
        numero de variables

    """

    def __init__(self, variables: int, implicantes: tuple):
        """
        Nuevo termino.
        NOTE: No usar esta funcion directamente para
              crear terminos. esta funcion no 
              regenera la representacion

        """
        self.implicantes = implicantes
        self.variables = variables
        self.representacion = ""

    def __str__(self):
        foo = self.representacion + " " + str(self.implicantes)
        return foo

    
    @classmethod
    def por_minterminos(cls, variables, implicantes):
        """
        Crear un Termino en base a sus implicantes

        """
        foo = Termino(variables, implicantes)
        foo.regenerar()
        return foo

    
    def combine(self, a):
        """
        Retorna la union de dos terminos

        """
        # elimina los valore repetidos y une las dos
        # tuplas de implicantes  
        implicantes = tuple(set(self.implicantes + a.implicantes))
        variables = self.variables
        foo = Termino.por_minterminos(variables, implicantes)
        return foo


    def regenerar(self):
        """
        Regenera la representacion del implicante, mantiene
        los terminos iguales 

        Ejemplo
        ----------
        Si unimos 8 y 9, 0b1000 y 0b1001 respectivamente, 
        la representacion deberia quedar así: '100-'.

        """
        # termino base
        b = bindigits(self.implicantes[0], self.variables)
        # output, uso una lista porque los string son datos
        # inmutables            
        output = [None] * self.variables  

        for implicante in self.implicantes:
            # termino para unir 
            a = bindigits(implicante, self.variables)

            for i in range(len(a)):
                # si son diferentes '-' si son iguales
                # mantiene el valor de el termino base
                output[i] = '-' if a[i] != b[i] else b[i]

            b = "".join(output)
        # convertir todo en un string
        self.representacion = "".join(output)

        
    def es_adyacente(self, b):
        """
        Verificar si se pueden unir los términos, en el 
        mapa de karnaugh se verían como sí fueran 
        adyacentes.

        """
        return diferencias(self.representacion,
                           b.representacion) == 1


# *********************************************************
#                          CODE
# *********************************************************


def extraer_primos(nvariables: int, terminos: list) -> list:
    """
    extrae los terminos del primos, que no se pueden 
    reducir.

    """
    a = []  # terminos iteracion actual
    b = []  # terminos de la siguiente iteracion

    # lista de terminos de implicantes primos
    primos = []  
    
    # lista de representaciones de los implicantes, se usa
    # para evitar duplicar terminos en 'primos'
    existentes = []  

    # crear la lista de terminos
    for termino in terminos:    
        a.append(Termino.por_minterminos(nvariables, [termino]))

        
    # sí hay terminos para reducir, todos son
    # primos, continua           
    while len(a) != 0:
        for i in a:
            cnv = 0             # numero de combinaciones
            for j in a:
                if not i.es_adyacente(j): continue
                # si son adyasentes significa
                # que se combinan
                cnv += 1
                termino = i.combine(j)

                # si no existe ese mintermino en la lista
                # de terminos se agrega a la lista
                if not (termino.representacion in existentes):
                    b.append(termino)
                    existentes.append(termino.representacion)

            # si no se combiina el termino es primo
            if cnv == 0: primos.append(i)

        a = b.copy()            # siguiente iteracion
        b = []

    # print(existentes)
        
    return primos


def esenciales(primos, minter):
    # posiciones de los términos esenciales, luego se
    # usara pop
    indice_esenciales = []
    minterminos_cubiertos = []

    # lista para guardar la lista al final
    foo = []

    # iterar los minterminos
    for i in minter:       
        
        # cantidad de veces que aparece el termino
        freq = 0
        # posiscion del termino esencial
        term = None
        
        for count, j in enumerate(primos):
            # si el mintermino no aparece en la lista de
            # implicantes del termino se salta
            if not i in j.implicantes: continue

            # si hay mas de un termino que contiene
            # el mintermino el termino NO es esencial y
            # termina la iteracion
            if freq == 1:
                # si el minitermino aparecido en otro termino
                # se elimina su posicion
                term = None
                break

            # si el minitermino no ha aparecido en otro termino
            # se guarda su posicion
            freq += 1
            term = count

        # si el minitermino no apareceio en otro termino
        # se guarda ni tampoco aparece en la lista de terminos 
        if term != None and not term in indice_esenciales :
            minterminos_cubiertos.append(i)
            indice_esenciales.append(term)

    # se extraen los terminos esenciales de la lista
    # de terminos primos y se sustituyen con None
    for i in indice_esenciales:
        foo.append(primos[i])
        primos[i] = None

    for i in indice_esenciales:
        minter[i] = None

    # se eliminan los None de la lista de primos
    remove_nones(minter)
    remove_nones(primos)

    return foo




# nvariables = 3
# minterminos = [3,4,5]
# redundancias = [1,6]



nvariables = 4
# minterminos = [4, 8, 10, 11, 12, 15]
# redundancias = [9, 14]

minterminos = [2,7,9,10,11,15]
redundancias = [1,8]

# minterminos = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# redundancias = []

# minterminos = [3,7,11,12,13,14,15]
# redundancias = []

# minterminos = [0,1,2,3,5,7,8,10,12,13,15]
# redundancias = []

# minterminos = [0,4,5,7,8,11,12,15]
# redundancias = []

# minterminos = [2,6,8,9,10,11,14,15]
# redundancias = []

# minterminos = [ 0,1,2,5,6,7,8,9,10,14]
# redundancias = []



todos_los_terminos = minterminos + redundancias

primos = extraer_primos(nvariables, todos_los_terminos)

terminos_esenciales = esenciales(primos, minterminos)

print("")

print("Esenciales")
for i in terminos_esenciales:
    print(i)

print("")

print("No Esenciales:", minterminos)
for i in primos:
    print(i)
