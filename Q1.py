n=int(input("enter a number:")) 
 if n<0: 
     print("invalid input,please enter positive integers") 
 elif n>0: 
     table=1 
     while table<21: 
         print(n,"x",table,"=",n*table) 
         table+=1
