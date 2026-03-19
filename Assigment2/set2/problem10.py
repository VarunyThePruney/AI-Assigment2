from CtoFandK import celcius_to_fahrenheit, celcius_to_kelvin

celcius = float(input("Enter temperature in Celsius: "))
fahrenheit = celcius_to_fahrenheit(celcius)
kelvin = celcius_to_kelvin(celcius)
print(f"{celcius}°C is equal to {fahrenheit}°F, and {kelvin}K.")