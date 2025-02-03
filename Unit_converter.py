def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

if __name__ == "__main__":
    print("Temperature Converter")
    print("----------------------")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        temp = float(input("Enter temperature in Celsius: "))
        print(f"{temp}°C = {celsius_to_fahrenheit(temp)}°F")
    elif choice == "2":
        temp = float(input("Enter temperature in Fahrenheit: "))
        print(f"{temp}°F = {fahrenheit_to_celsius(temp)}°C")
    elif choice == "3":
        temp = float(input("Enter temperature in Celsius: "))
        print(f"{temp}°C = {celsius_to_kelvin(temp)}K")
    elif choice == "4":
        temp = float(input("Enter temperature in Kelvin: "))
        print(f"{temp}K = {kelvin_to_celsius(temp)}°C")
    else:
        print("Invalid choice!")
