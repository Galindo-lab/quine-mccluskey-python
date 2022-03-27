
IMPLICANTS = 0
BIN = 1

def count_set_bits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count

def bindigits(number,digits):
    # numero binario, de bit fijos
    return "{0:0{1}b}".format(number,digits)

def implicants_table(m,d,n):
    f = m + d
    f.sort(key=count_set_bits)
    table = [ [[e],bindigits(e,n)] for e in f ]
    return table

def join_bin(a,b):
    output = []
    for i in range(len(a)):
        output.append( '-' if a[i] != b[i] else a[i] )
    return "".join(output)

def join_row(a,b):
    foo = a[IMPLICANTS]+b[IMPLICANTS]
    foo.sort()
    return [ foo , join_bin(a[BIN],b[BIN]) ]

def count_ones(a):
    return a.count("1")

def bit_diff(a,b):              # numero de bits diferentes
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
    return diff

def find_primes(m):
    table = []
    for a in m:
        is_prime = True
        for b in m:
            if bit_diff(a[BIN],b[BIN]) == 1:
                is_prime = False
                break
        if is_prime:
            table.append(a)
    return table

def remove_columns(table, primes):
    for i in primes:
        table.remove(i)

def simp(m):
    table = []
    for a in m:
        for b in m:
            if a != b and bit_diff(a[BIN],b[BIN]) == 1:
                c = join_row(a,b)
                if c not in table:
                    table.append(c)                
    return table

# numero de variables
n = 5

# valores de activacion
m = [0,2,3,5,7,8,10,11,13,15,22,29,30]

# valores indiferentes
d = []


# -----------------
print(" Running... ")

def tabulate(m,d,n):
    tabla = implicants_table(m,d,n)
    mint = []
    while(True):
        p = find_primes(tabla)
        mint += p
        remove_columns(tabla,p)
        tabla = simp(tabla)
        if len(tabla) == 0:
            break
    return mint
