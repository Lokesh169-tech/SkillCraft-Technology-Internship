
print("TEMPERATURE CONVERTER")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

choice = int(input("Enter your choice: "))
temp = float(input("Enter temperature: "))

if choice == 1:
    result = (temp * 9/5) + 32
elif choice == 2:
    result = (temp - 32) * 5/9
elif choice == 3:
    result = temp + 273.15
elif choice == 4:
    result = temp - 273.15
elif choice == 5:
    result = (temp - 32) * 5/9 + 273.15
elif choice == 6:
    result = (temp - 273.15) * 9/5 + 32
else:
    print("Invalid choice")
    exit()

print("Converted Temperature:", round(result, 2))
