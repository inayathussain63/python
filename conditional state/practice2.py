#WAP TO find the greatest of 3 numbers entered by the user 
a = int(input("Enter your first number:"))
b = int(input("Enter your second number:"))
c = int(input("Enter your three number:"))

if(a>=b and a>=c):
    print("a is the greatest number:", a )
elif(b>=c):
    print("b is the greatest number:", b) 
    
else:
    print("c is the greatest number:", c)       