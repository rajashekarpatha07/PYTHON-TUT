def celsius_to_fahrenheit_heat(c):
    if c == 32:
        return c
    else:
        result = (c * 9/5) + 32
        return result

celsius = int(input("Enter celsius: "))

result = celsius_to_fahrenheit_heat(celsius)
print(f"{celsius} celsius = {round(result)} Fahrenheit")