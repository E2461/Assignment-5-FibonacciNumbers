def fibo_cal(nterms):
   
    list_fibo = []
   
    n1, n2 = 0, 1
    count = 0
    while count < nterms:
       list_fibo.append(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
    return(list_fibo)
    

print(fibo_cal(11))

