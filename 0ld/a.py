# Python3 program for the above approach
def sumBitDiff(arr):
    diff = 0    #hold the ans
       
    for i in range(len(arr)):
        for j in range(i, len(arr)):
               
        # XOR toggles the bits and will form a number that will have
        # set bits at the places where the numbers bits differ
        # eg: 010 ^ 111 = 101...diff of bits = count of 1's = 2          
            xor = arr[i]^arr[j]
            count = countSetBits(xor)        #Integer.bitCount() can also be used
                   
            # when i == j (same numbers) the xor would be 0,
            # thus our ans will remain unaffected as (2*0 = 0)
            diff += (2*count)
       
    return diff
     
# Kernighan algo
def countSetBits(n):
    count = 0            # `count` stores the total bits set in `n`
  
    while (n != 0) :
        n = n & (n - 1)    # clear the least significant bit set
        count += 1
         
    return count
     
# Driver code
if __name__ == "__main__":
     
    arr = [5,10]
    ans  = sumBitDiff(arr)
    print(ans)
 
    # This code is contributed by sanjoy_62.
