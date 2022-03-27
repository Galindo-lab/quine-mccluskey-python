def combine_implicants(a: str,b :str) -> str:
    """Crea la tabla de implicantes de primer orden

    Parameters
    ----------
    a : str
        Implicantes en binario
    b : str
        Implicantes en binario

    Returns
    -------
    list
        Union de los dos implicantes, los valores variantes se reemplazan con el caranter '-'
    """    
    output = []
    for i in range(len(a)):
        output.append( '-' if a[i] != b[i] else a[i] )
    return "".join(output)

