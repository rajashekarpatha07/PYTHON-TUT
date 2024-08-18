age = int(input("Enter you are age: "))


if(age%2 == 0):
    print("Its a n even number")
if (age>18):
    print("You are Elgible for driving...!")
elif(age<0):
    print("The age is invalid!!")
elif(age==0):
    print("You are entered age zero which is not valid")
else:
    print("You are not elgible for driving ")