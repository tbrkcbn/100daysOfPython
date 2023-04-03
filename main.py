# variable definitions:
choice = ""
water = 1000
coffeeGrains = 1000
milk = 1000
money = 0
# class definitions

# function definitions

def report():
    print(f"Water:   {water}ml")
    print(f"Coffee:  {coffeeGrains}ml")
    print(f"Milk:    {milk}ml")
    print(f"Money:   {money}$")

# main loop cycle

while not choice == "off":
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice  == "espresso":
        print
    elif choice  == "report":
        report()
    elif choice  == "latte":
        print
    elif choice  == "cappuccino":
        print
    else :
        print("Choose again")

print("Adios amigo!")