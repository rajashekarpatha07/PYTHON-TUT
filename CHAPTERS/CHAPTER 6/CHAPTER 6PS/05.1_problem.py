#  Write a program which finds out whether a given name is present in a list or not
names = ["raj", "sai", "purna","nikhil"]

username = input("Enter the name you want to find in lsit: ").lower()

if username in names:
    index = names.index(username)
    print(f"Yes, The {username} is present in list in index {index}")
else:
    print("Your name is not in the list")