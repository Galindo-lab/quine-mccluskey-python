import math

def bin(number):
    digits = 8
    # mejor formato de binario
    return "{0:0{1}b}".format(number,digits)

def countSetBits(n):
    # enontrar el numero de bits
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count

def ordenar(m):
    # NOTE Metodo destructivo
    # ordena por numeros de bits 'Verdaderos'
    m.sort(key=countSetBits)

def adyasentes(a, b):
    # NOTE Sí es el mismo numero retorna 'Falso'
    # encontrar si dos valores son adyasentes en el mapa de karnouhgt
    return countSetBits(a^b) == 1

def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

def mor(a):
    return reduce( lambda x,y: x^y, a )


print("") # --------------------------

# https://www.ecured.cu/M%C3%A9todo_de_Quine-McCluskey
#m = [1, 3, 4, 5, 7, 9, 10, 11, 15]
#m = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
m = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
variables = 6

ordenar(m)
m1 = []
m2 = []
m3 = []

# https://es.wikipedia.org/wiki/Mapa_de_Karnaugh
renglones = int(math.sqrt(2**variables))
print(renglones)

for a in range(len(m)):
    for b in range(a,len(m)):  
        if adyasentes(m[a],m[b]) :
            print((m[a],m[b]))
            m1.append((m[a],m[b]))

print("----------------------------------")
for a in range(len(m1)):
    for b in range(a,len(m1)):  
        c = sum(m1[a])
        d = sum(m1[b])
        if adyasentes(c,d) and countSetBits(mor(m1[a]+m1[b])) == 0:
            m2.append(m1[a]+m1[b])
            print(m1[a]+m1[b] )

print("----------------------------------")
for a in range(len(m2)):
    for b in range(a,len(m2)):  
        c = sum(m2[a])
        d = sum(m2[b])
        if adyasentes(c,d) and countSetBits(mor(m2[a]+m2[b])) == 0:
            m3.append(m2[a]+m2[b])
            print(m2[a]+m2[b] )


print("----------------------------------")
for a in range(len(m3)):
    for b in range(a,len(m3)):  
        c = sum(m3[a])
        d = sum(m3[b])
        if adyasentes(c,d) and countSetBits(mor(m3[a]+m3[b])) == 0:
            print(m3[a]+m3[b] )



# print("----------------------------------")
# for a in range(len(m1)):
#     for b in range(a,len(m1)):  
#         c = sum(m1[a])
#         d = sum(m1[b])
#         if adyasentes(c,d) and countSetBits(m1[a][0]^m1[a][1] ^ m1[b][0]^m1[b][1] ^ 0b0) ==0:
#             m2.append(m1[a]+m1[b])
#             print(m1[a]+m1[b] )

# print("----------------------------------")
# for a in range(len(m2)):
#     for b in range(a,len(m2)):  
#         c = sum(m2[a])
#         d = sum(m2[b])
#         if adyasentes(c,d) and countSetBits(m2[a][0]^m2[a][1] ^ m2[b][0]^m2[b][1] ^ 0b0) ==0:
#             # m2.append(m2[a]+m2[b])
#             print(m2[a]+m2[b] )
            
