# Una funcion para mostrar numeros binarios
# de una manera más util

# Origen:
# https://stackoverflow.com/a/12946226

def bindigits(n, bits):
    s = bin(n & int("1"*bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)



