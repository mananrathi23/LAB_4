n= int(input("Enter an integer: ")) 
if n > 1: 
        i=2 
        while i*i<=n: 
        if n%i==0: 
            print("it is not a prime number") 
            break 
        i+=1 
  
        else: 
              print( "it is a prime number") 
elif n<0: 
        print("invalid case ,please enter the positive value") 
elif n==1 or n==0:         
        print("0 or 1 are not prime numbers")
