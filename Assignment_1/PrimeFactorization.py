import pdb
import math as  m
def isPrime(value):
    """
    Checks give number is prime number or not
    """
    x=int(m.sqrt(value))
    
    for i in range (2,x+1):
        if(value%i==0):
            return False
    return True    
def getPrime(currval):
    """
    gives the next prime number based on the current prime number 
    """
    flag =0
    for i in range(currval,100000,2):
        x=int(m.sqrt(i))
        for j in range(2,x+1):
            if(i%j==0):
                flag=1

                break
            else:
                continue
        if flag==0:

            return i
        
######Start######
n = int(input("Enter the value to find primeFactorization :"))
lis=[1]
i=2
while(isPrime(n)==False):
    if(n%i==0):
        lis.append(i)

        n=int(n/i)

    else:
        if(i==2):

            i=getPrime(i+1)
            
        else:

            i=getPrime(i+2)
else:
    lis.append(n)
print(lis)
