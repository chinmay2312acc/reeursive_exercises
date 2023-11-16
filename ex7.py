def sum_odd(num) :
    if(num%2==0) :
        if(num <=0) :
            return 0
        
        else:
            return num -1 + sum_odd(num-2) 
    else :
      #  num = num - 1
        if num<=0 :
            return 0
        else :
            return num + sum_odd( num -2 ) 
        
print(sum_odd(11))