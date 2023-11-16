list1=[]
def rec(num) :
    if(num%2==0) :
        
        if(num==1) :
            return 1
        
        else :
            return rec(num/2)
        
    else :
        if(num==1) :
            return 1 
        else :
            return rec((3*num)+1)
        
print(rec(6))