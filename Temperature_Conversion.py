# Celsius to Fahrenheit
def cf(c):
    return (1.8*c)+32

# Fahrenheit to Celsius
def fc(f):
    return 0.555*(f-32)

# Celsius to Kelvin
def ck(c):
    return c+273.15

# Fahrenheit to Kelvin
def fk(f):
    return (f+459.67)*0.555


print("-MENU-")
print("1.Celsius to Fahrenheit")
print("2.Fahrenheit to Celsius")
print("3.Celsius to Kelvin")
print("4.Fahrenheit to Kelvin")

while True:
    # Gather user's input
    opt = input("Enter option (1-4): ")

    # Check what operation the user wants then print result
    if opt in ('1', '2', '3', '4'):

        if opt == '1':
            cel = float(input("Enter temperature in Celsius:"))
            print("Temperature in Fahrenheit is:")
            print(cf(cel))

        elif opt == '2':
            fahr = float(input("Enter temperature in Fahrenheit:"))
            print("Temperature in Celsius is:")
            print(fc(fahr))

        elif opt == '3':
            cel = float(input("Enter temperature in Celsius:"))
            print("Temperature in Kelvin is:")
            print(ck(cel))

        elif opt == '4':
            fahr = float(input("Enter temperature in Fahrenheit:"))
            print("Temperature in Kelvin is:")
            print(fk(fahr))
        break

    else:
        print("Invalid Option!!") 
