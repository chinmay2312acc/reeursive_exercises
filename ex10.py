def fact(num) :
    if num==1 :
        return 1
    else :
        return num*fact(num-1)

def euler(n) :
    if n ==0 :
        return 1
    else :
        return 1/fact(n) + euler(n-1) 

print(fact(5))
print(euler(4))