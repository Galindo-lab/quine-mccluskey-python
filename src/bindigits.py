
def bindigits(number: int,digits: int) -> str:
    """Convertir numero a binario

    Parameters
    ----------
    number : int
        Numero a convertir a binario
    digits : int
        Numero de dígitos en la representación binaria

    Returns
    -------
    str
        representación binaria del entero
    """
    return "{0:0{1}b}".format(number,digits)
