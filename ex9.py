def rec(n) :
    if n<=1 :
        return 4
    else :
        return ((pow(-1,n+1))*(4/((2*n)-1))) + rec(n-1)
print(rec(3))
    
        