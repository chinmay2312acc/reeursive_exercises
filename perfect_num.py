 def fact(n) :
     fact_list=[]
     count =1
     while count <=n/2 :
         if(n%count ==0) :
             fact_list.append(n)
             count = count +1 
        
        else :
            count = count + 1 