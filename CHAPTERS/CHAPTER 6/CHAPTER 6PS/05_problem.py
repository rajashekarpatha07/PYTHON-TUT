dic = {
    "raj": 10,
    "sai": 6,
    "purna": 7,
    "nikhil": 9
}

name = input("Enter the name you want to find in dic: ")

if name in dic:
    print(f"Yes, the name {name} is present in dic with a value of {dic.get(name)}")
else:
    print(f"The name {name} is not present in dic.")
