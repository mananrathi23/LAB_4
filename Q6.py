n = int(input("Enter a positive integer: ")) 
if n < 0: 
    print("Please enter a positive integer.") 
else: 
    X=n   
    reverse =0 
    while n > 0: 
        temp = n % 10 
        reverse= reverse*10 +temp 
        n //= 10 
    if reverse==X: 
          print("palindrome") 
    else: 
        print("not a palindrome")
