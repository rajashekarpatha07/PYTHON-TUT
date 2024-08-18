def gratest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

result = gratest(a,b,c)

print(f"the gratest number in {a}, {b}, {c} is {result}")