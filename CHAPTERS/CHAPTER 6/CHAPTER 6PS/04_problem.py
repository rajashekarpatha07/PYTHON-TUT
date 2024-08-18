Username = input("Enter user name: ")
length = len(Username)

if length<10:
    print(f"yes this {Username} contain {length} charactors and less than 10 charactors")
else:
    print(f"{Username} contain {length} charactors")