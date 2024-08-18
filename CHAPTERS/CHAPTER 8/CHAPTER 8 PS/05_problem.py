def inches_to_cm(inches):
    result = inches*2.5
    return result


inches = int(input("Enter inches: "))

result = inches_to_cm(inches)

print(f"{inches} inches = {round(result)} cm")
