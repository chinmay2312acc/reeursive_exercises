def rec (value) :
    
    if value/10 <= 0 :
        return 0
    else :
        return value%10 + rec(value//10)
    
#print(1567//10)
    
print(rec (12360000000003))