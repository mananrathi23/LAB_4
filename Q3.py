x=int(input("enter a number:")) 
y=int(input("enter a number:")) 
n=int(input("enter a number:")) 
if x<y: 
  i=x+1 
    while i>x and i<=y :
      if i%n==0:
        print(i)
        i+=1 
elif x>y: 
  print("invalid case , y must be greater then x")
