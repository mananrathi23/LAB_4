n = int(input("Enter a positive integer: ")) 
 if n < 0: 
     print("invalid input , Please enter a positive integer.") 
 else:   
     sum =0 
     while n>0: 
         temp = n % 10 
         sum += temp 
         n =n // 10 
     print("sum of all digits of given number is ",sum)
