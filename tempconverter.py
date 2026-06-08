#temperature conversion

temperature = float(input("Enter your temperature: "))
unit = input("Enter your unit(C or F): ")

if unit == "C":
    temperature = (temperature * 9/5) + 32
    unit = "Fahrenheit"
    print (f" the temperature is {round(temperature)} {unit}")
elif unit == "F":
    temperature = (temperature - 32) * 5/9
    unit = "Celcius"
    print(f" the temperature is {round(temperature)} {unit}")
else:
    print (f"{unit} is invalid")