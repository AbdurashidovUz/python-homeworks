

def convert_cel_to_far(celsius):
    return celsius * 9/5 + 32

def convert_far_to_cel(fahrenheit):
    return (fahrenheit - 32) * 5/9

celcius = int(input("Enter the temperature in celcius: "))
fahrenheit = convert_cel_to_far(celcius)
print(f"{celcius}°C is equal to {round(fahrenheit,2)}°F")

fahrenheit = int(input("Enter the temperature in fahrenheit: "))
celcius = convert_far_to_cel(fahrenheit)
print(f"{fahrenheit}°F is equal to {round(celcius,2)}°C")