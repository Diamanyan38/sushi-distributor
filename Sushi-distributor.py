# Define Variables

print("Welcome to Sushi Distributor!")
print("There is multiple Sushi type available")

# List of differents sushis with prices
print("1: Normal Sushi - 20$")
print("2: Luxery Sushi - 50$")
print("3: Lasagna Sushi - 80$")
print("4: SUSSY Sushi - 6969$")

choise = input("Enter your choise: ")

if choise == 1:
    print("You choosed: Normal Sushi")
    money = input("Enter your money amount: ")
    if money < 20:
        print("Sorry, no sushi for you.")
    else: 
        print("Take your sushi! 🍣")

if choise == 2:
    print("You choosed: Luxery Sushi")
    money = input("Enter your money amount: ")
    if money < 50:
        print("Sorry, no sushi for you.")
    else: 
        print("Take your sushi! 🍣")
if choise == 3:
    print("You choosed: Lasagna Sushi")
    money = input("Enter your money amount: ")
    if money < 80:
        print("Sorry, no sushi for you.")
    else: 
        print("Take your sushi! 🍣")

if choise == 4:
    print("You choosed: SUSSY Sushi")
    money = input("Enter your money amount: ")
    if money < 6969:
        print("Sorry, no sushi for you.")
    else: 
        print("Take your sushi! 🍣")
