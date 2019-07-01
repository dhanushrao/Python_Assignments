def multiplication(n,size=10):
    num=0
    for i in range(1,size+1):
        num=i*n
        print("{0}*{1}={2}".format(n,i,num))
multiplication(2,5)
