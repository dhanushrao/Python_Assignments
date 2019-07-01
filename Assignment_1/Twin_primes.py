#This program is used to find twin from 0 to 100 
import math as m  
def isPrime(value):
"""Checks wheather the given number is prime or not"""
    x=int(sqrt(value))
    
    for i in range (2,x+1):
        if(value%i==0):
            return False
    return True    
for i in range (3,1000,2):
    if(i%2!=0):
        if(isPrime(i) and isPrime(i+2)):
            print("({0},{1})".format(i,i+2))
        else:
            continue
