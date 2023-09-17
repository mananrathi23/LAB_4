a=int(input("enter a coefficient of x2:")) 
b=int(input("enter a coefficient of x:")) 
c=int(input("enter a constant ,c :")) 
print("quadratic equation is :",a,"x^2 +",b,"x +",c) 
d=(b**2-4*a*c) 
x1=(-b+(d)**(1/2))/(2*a) 
x2=(-b-(d)**(1/2))/(2*a) 
if d>0: 
  print("roots are real",x1,x2) 
elif d==0: 
  print ("roots are same ",x1,x2) 
else: 
  print("roots are imaginary",x1,x2)
