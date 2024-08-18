age = {
    "Raj": 18,
    "sai": 16,
    "nikhil": 21
}
print(age["nikhil"])
# print(age.items()) #Method Used to Return the Items in dictionory

# print(age.keys()) #Method Used to return the keys Eg:Raj, sai, nikhil is the keys

# print(age.values()) #Method used to return the values associated to keys

# age.update({"Raj": 17, "purna": 15}) #Method used to update existing item and adding new item to list
# print(age["Raj"])

print(age.get("sai1")) #returns none

print(age["sai1"]) #returns error