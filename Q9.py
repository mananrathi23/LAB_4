X=input("enter a sentence") 
capital=0 
small=0 
digit=0 
special=0 
index=0 
while index<len(X): 
    char=X[index] 
    if 'A'<=char<='Z': 
        capital+=1 
    elif 'a'<=char<='z': 
        small+=1 
    elif '0'<=char<='9': 
        digit+=1 
    else: 
        special+=1  
    index+=1          
print(capital) 
print(small)  
print(digit) 
print(special)
