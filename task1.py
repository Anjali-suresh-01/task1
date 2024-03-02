def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

temperature = float(input("Enter the temperature value: "))
unit = input("Enter the unit of measurement (Celsius, Fahrenheit, or Kelvin): ").lower()

if unit == "celsius":
    print(f"{temperature} Celsius is equal to {celsius_to_fahrenheit(temperature)} Fahrenheit")
    print(f"{temperature} Celsius is equal to {celsius_to_kelvin(temperature)} Kelvin")
elif unit == "fahrenheit":
    print(f"{temperature} Fahrenheit is equal to {fahrenheit_to_celsius(temperature)} Celsius")
    print(f"{temperature} Fahrenheit is equal to {fahrenheit_to_kelvin(temperature)} Kelvin")
elif unit == "kelvin":
    print(f"{temperature} Kelvin is equal to {kelvin_to_celsius(temperature)} Celsius")
    print(f"{temperature} Kelvin is equal to {kelvin_to_fahrenheit(temperature)} Fahrenheit")
else:
    print("Invalid unit of measurement. Please enter Celsius, Fahrenheit, or Kelvin.")
