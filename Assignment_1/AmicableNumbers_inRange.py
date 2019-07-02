import pdb
from functools import reduce
def sumPdivisors(num,hashMap):
    if(num!=1):
        x = int(num/2)
        lis=[i for i in range(1,x+1) if num%i==0]
        x=reduce(lambda x,y:x+y,lis)
        if x in hashMap:
# checks if the sumOfdivisor is present in the map as a key
            if(hashMap[x]==num):
#         if present checks the value of that key is equal to current number if yes both are amicable numbers 
                print("({0},{1})".format(x,num))
#     Stores the key in hash map and returns the hashMap
        hashMap[num]=x
        return hashMap

        
# An Empty Hash map is used to store the key as number and the sum of divisiors as values
hashMap={}
start = int(input("Enter the starting number "))
end = int (input("Enter the ending range "))
for  i in range(start,end+1):
#     Every time new hash map is returned with new key value pair
        hashMap=sumPdivisors(i,hashMap)
