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
def seconds_to_minutes(seconds):
    return seconds / 60

def minutes_to_hours(minutes):
    return minutes / 60

def hours_to_days(hours):
    return hours / 24

def days_to_weeks(days):
    return days / 7

def get_numeric_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")


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
    print("13. Seconds to Minutes")
    print("14. Minutes to Hours")
    print("15. Hours to Days")
    print("16. Days to Weeks")
    print("17. Exit")
    
    choice = input("Enter your choice: ")
    
if choice == "1":
            temp = get_numeric_input("Enter temperature in Celsius: ")
            print(f"{temp}°C = {celsius_to_fahrenheit(temp)}°F")
elif choice == "2":
            temp = get_numeric_input("Enter temperature in Fahrenheit: ")
            print(f"{temp}°F = {fahrenheit_to_celsius(temp)}°C")
elif choice == "3":
            temp = get_numeric_input("Enter temperature in Celsius: ")
            print(f"{temp}°C = {celsius_to_kelvin(temp)}K")
elif choice == "4":
            temp = get_numeric_input("Enter temperature in Kelvin: ")
            print(f"{temp}K = {kelvin_to_celsius(temp)}°C")
elif choice == "5":
            length = get_numeric_input("Enter length in meters: ")
            print(f"{length}m = {meters_to_kilometers(length)}km")
elif choice == "6":
            length = get_numeric_input("Enter length in kilometers: ")
            print(f"{length}km = {kilometers_to_meters(length)}m")
elif choice == "7":
            length = get_numeric_input("Enter length in miles: ")
            print(f"{length} miles = {miles_to_feet(length)} feet")
elif choice == "8":
            length = get_numeric_input("Enter length in feet: ")
            print(f"{length} feet = {feet_to_miles(length)} miles")
elif choice == "9":
            weight = get_numeric_input("Enter weight in kilograms: ")
            print(f"{weight}kg = {kilograms_to_grams(weight)}g")
elif choice == "10":
            weight = get_numeric_input("Enter weight in grams: ")
            print(f"{weight}g = {grams_to_kilograms(weight)}kg")
elif choice == "11":
            weight = get_numeric_input("Enter weight in pounds: ")
            print(f"{weight} lbs = {pounds_to_ounces(weight)} oz")
elif choice == "12":
            weight = get_numeric_input("Enter weight in ounces: ")
            print(f"{weight} oz = {ounces_to_pounds(weight)} lbs")
elif choice == "13":
            time = get_numeric_input("Enter time in seconds: ")
            print(f"{time} seconds = {seconds_to_minutes(time)} minutes")
elif choice == "14":
            time = get_numeric_input("Enter time in minutes: ")
            print(f"{time} minutes = {minutes_to_hours(time)} hours")
elif choice == "15":
            time = get_numeric_input("Enter time in hours: ")
            print(f"{time} hours = {hours_to_days(time)} days")
elif choice == "16":
            time = get_numeric_input("Enter time in days: ")
            print(f"{time} days = {days_to_weeks(time)} weeks")
elif choice == "17":
            print("Exiting the converter. Goodbye!")
            break
else:
    print("Invalid choice! Please enter a number between 1 and 17.")

