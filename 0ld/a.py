

# https://www.geeksforgeeks.org/count-set-bits-in-an-integer/
def countSetBits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count

# m = [4,8,9,10,11,12,14,15]
# m = [0,1,11,13,15]
# m = [0,1,2,5,6,7]

# https://docplayer.es/22156298-Metodo-de-simplificacion-de-funciones-logicas-utilizando-el-metodo-de-quine-mccluskey.html
#m = [0,2,3,5,7,8,10,11,13,15,22,29,30]

#m = [2,6,8,9,10,11,14,15]
#m = [0,3,5,6,9,10,12,15,18,20,21,24,25,27,30,33,35,36,39,40,42,45,48,50,51,54,55,57,60,63]

# m = [0,2,3,5,7,8,10,11,13,15,22,19,30]
m = [2,3,5,8,10,11,12,13,14,15]

m.sort(key=countSetBits)

mi1 = []
mi2 = []

print("-----1------")

for a in m:
    for b in m:
        if a-b>0 and countSetBits(a) != countSetBits(b) and countSetBits(a^b) == 1:
            mi1.append((a,b))
            print((a,b),bin(a^b))

print("---2--------")

for c in mi1:
    for d in mi1:
        a = sum(c)
        b = sum(d)
        if a-b>0 and countSetBits(a) != countSetBits(b) and countSetBits(a^b) == 1 and countSetBits( (c[0]^c[1])^(d[0]^d[1]) ) == 0:
            mi2.append(c+d  )
            print(c+d,bin((c[0]^c[1])^(d[0]^d[1])))

print("---3--------")
            
for c in mi2:
    for d in mi2:
        a = sum(c)
        b = sum(d)
        if a-b>0 and countSetBits(a) != countSetBits(b) and countSetBits(a^b) == 1 and countSetBits( (c[0]^c[1])^(d[0]^d[1]) ) == 0:
            print(c+d,bin(a),bin(b))
