def GCD(n1,n2,) :
    if(n1 == 0) :
        return n2
    elif(n2 ==0) :
        return n1
    else :
        return GCD(n2,n1%n2)
    
def LCM(n1,n2) :
    return (n1*n2)/GCD(n1,n2)


print(LCM(2,4))