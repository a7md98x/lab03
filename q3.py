def celsiustoFahrenheit(cel):
    return 9/5*cel+32

x = float(input("enter tempreture in celsius: "))

print(f"the tempreture in Fahrenheit is : {celsiustoFahrenheit(x)} F")