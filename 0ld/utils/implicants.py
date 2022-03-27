# extrae los valores implicantes de un grupo, los bits que no cambian
# source: https://stackoverflow.com/a/12790495
# ejmplo:
# 4,6,12,14 = ('0b100', '0b110', '0b1100', '0b1110')
#           |
#           +----0b101

def implicants(n):
    foo = n[0]
    bar = (~n[0] & 0xF)
    for i in range(1, len(n)):
        foo &= n[i]
        bar &= (~n[i] & 0xF)
    return ( foo + bar ) 
