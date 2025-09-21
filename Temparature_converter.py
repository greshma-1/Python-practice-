def temperature_converter():
    print("Temperature Converter")
    temp = float(input("Enter temperature: "))
    unit = input("Convert from (C/F/K): ").upper()

    if unit == "C":
        print(f"Fahrenheit: {(temp * 9/5) + 32}")
        print(f"Kelvin: {temp + 273.15}")
    elif unit == "F":
        print(f"Celsius: {(temp - 32) * 5/9}")
        print(f"Kelvin: {(temp - 32) * 5/9 + 273.15}")
    elif unit == "K":
        print(f"Celsius: {temp - 273.15}")
        print(f"Fahrenheit: {(temp - 273.15) * 9/5 + 32}")
    else:
        print("Invalid unit")

temperature_converter()
