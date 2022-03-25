# contar el numero de '1' en una numero binari

# origen:
# https://www.geeksforgeeks.org/count-set-bits-in-an-integer/

def count_set_bits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count
