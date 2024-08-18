def Perimeter_of_rectangle(l ,b):
    perimeter = 2*l+b
    print(f"The perimeter of rectangle is \n{perimeter}")
    
def Greater(l, b):
    if l>b:
        print(f"The length {l} is greater than breadth {b}")
    else:
        print(f"The breadth {b} is greather than length {l}")
        
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

Perimeter_of_rectangle(length, breadth)
Greater(length, breadth)

    