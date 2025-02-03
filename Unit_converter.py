def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def meters_to_kilometers(meters):
    return meters / 1000

def kilometers_to_meters(kilometers):
    return kilometers * 1000

def miles_to_feet(miles):
    return miles * 5280

def feet_to_miles(feet):
    return feet / 5280
def kilograms_to_grams(kg):
    return kg * 1000

def grams_to_kilograms(g):
    return g / 1000

def pounds_to_ounces(pounds):
    return pounds * 16

def ounces_to_pounds(ounces):
    return ounces / 16

if __name__ == "__main__":
    print("Temperature Converter")
    print("----------------------")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Meters to Kilometers")
    print("6. Kilometers to Meters")
    print("7. Miles to Feet")
    print("8. Feet to Miles")
    print("9. Kilograms to Grams")
    print("10. Grams to Kilograms")
    print("11. Pounds to Ounces")
    print("12. Ounces to Pounds")
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
    elif choice == "5":
        length = float(input("Enter length in meters: "))
        print(f"{length}m = {meters_to_kilometers(length)}km")
    elif choice == "6":
        length = float(input("Enter length in kilometers: "))
        print(f"{length}km = {kilometers_to_meters(length)}m")
    elif choice == "7":
        length = float(input("Enter length in miles: "))
        print(f"{length} miles = {miles_to_feet(length)} feet")
    elif choice == "8":
        length = float(input("Enter length in feet: "))
        print(f"{length} feet = {feet_to_miles(length)} miles")
    elif choice == "9":
        weight = float(input("Enter weight in kilograms: "))
        print(f"{weight}kg = {kilograms_to_grams(weight)}g")
    elif choice == "10":
        weight = float(input("Enter weight in grams: "))
        print(f"{weight}g = {grams_to_kilograms(weight)}kg")
    elif choice == "11":
        weight = float(input("Enter weight in pounds: "))
        print(f"{weight} lbs = {pounds_to_ounces(weight)} oz")
    elif choice == "12":
        weight = float(input("Enter weight in ounces: "))
        print(f"{weight} oz = {ounces_to_pounds(weight)} lbs")
    else:
        print("Invalid choice!")
