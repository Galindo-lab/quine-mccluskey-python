
def difference(a,b):
    """Comṕara dos strings y compara cuantos caracteres son diferentes 

    Parameters
    ----------
    a : String
    b : String

    Returns
    -------
    str
        Numero de diferecias
    """
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
    return diff
