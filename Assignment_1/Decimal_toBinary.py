def function (val):
    n = int(val /2)
    lis=[]
    if(n!=1):
        lis.append(val%2)
        lis.extend(function(n))
        return lis
    else:
        return [int(val%2),n]
lis=function(int(input("Enter the value to convert into binary")))
lis.reverse()
x=str(lis)
print(x)
