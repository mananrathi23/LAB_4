N=int(input("enter a number:")) 
 count1=0 
 count2=0 
while True:
  X=int(input("enter a number:"))
  if X==-999: 
  break
  elif (X%N==0): 
    count1+=1 
  elif (X%N!=0):  
    count2+=1         
print("total no. of inputs that are divisible by N are :",count1) 
print("total no. of inputs that are not divisible by N are :",count2)
