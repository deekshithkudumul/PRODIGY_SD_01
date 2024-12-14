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

def convert_temperature(value, unit):
    if unit == 'C':
        f = celsius_to_fahrenheit(value)
        k = celsius_to_kelvin(value)
        return f"{value}°C is {f:.2f}°F and {k:.2f}K"
    elif unit == 'F':
        c = fahrenheit_to_celsius(value)
        k = fahrenheit_to_kelvin(value)
        return f"{value}°F is {c:.2f}°C and {k:.2f}K"
    elif unit == 'K':
        c = kelvin_to_celsius(value)
        f = kelvin_to_fahrenheit(value)
        return f"{value}K is {c:.2f}°C and {f:.2f}°F"
    else:
        return "Invalid unit"

# Example usage
value = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
print(convert_temperature(value, unit))
