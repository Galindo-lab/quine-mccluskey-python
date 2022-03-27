
def count_set_bits(n: int) -> int:
    """Cuenta cuantos '1' aparecen en un string

    Parameters
    ----------
    n : int
        Cuenta el numero de '1' en un numero

    Returns
    -------
    int 
        numero de veces que aparece '1' en un entero
    """
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count
