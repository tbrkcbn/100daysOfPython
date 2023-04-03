# variable definitions:
choice = ""
water = 1000
coffeeGrains = 1000
milk = 1000
money = 0
change = 0

# -requirements
# latte: 
#     milk:   100
#     coffee: 100
#     water:  0
# espresso:
#     milk:   0
#     coffee: 100
#     water:  0
# cappuchino:
#     milk:   0
#     coffee: 100
#     water:  100

# function definitions
def checkResources(reqMilk,reqCoffee,reqWater):
    if reqWater <= water and reqCoffee <= coffeeGrains and reqMilk <= milk:
        return 1
    else:
        return 0

def checkOut(fee,water,coffee,milk):
    quarterNum = int (input("How many quarters?: "))
    dimeNum = int (input("How many dimes?: "))
    nickelNum = int (input("How many nickels?: "))
    pennyNum = int (input("How many pennies?: ") ) 
    total = (quarterNum*25+dimeNum*10+nickelNum*5+pennyNum)/100
    change = total - fee  

    if change < 0:
        print("Not enought money, here is your money back!")
    else:
        reduceMateriels(water,coffee,milk,fee)
        print(f"You give {total}$ and your change is {change}$ ...")

def reduceMateriels(usedWater,usedCoffee,usedMilk,gainedMoney):
    global water
    global coffeeGrains
    global milk
    global money
    water -= usedWater
    coffeeGrains -= usedCoffee
    milk -= usedMilk
    money += gainedMoney

def report():
    print(f"Water:   {water}ml")
    print(f"Coffee:  {coffeeGrains}gr")
    print(f"Milk:    {milk}ml")
    print(f"Money:   {money}$")

# main loop cycle

while not choice == "off":
    choice = input("What would you like? (espresso/latte/cappuccino):")

    if choice  == "espresso":
        if checkResources(0,100,0) == 1:
            checkOut(float (1.7),0,100,0)
        else:
            print("Insufficient material :( ")

    elif choice  == "report":
        report()
    elif choice  == "latte":
        if checkResources(0,100,100) == 1:
            checkOut(float (2.1),0,100,100)
        else:
            print("Insufficient material :( ")
    elif choice  == "cappuccino":
        if checkResources(100,100,0) == 1:
            checkOut(float (1.3),100,100,0)
        else:
            print("Insufficient material :( ")
    elif choice  == "off":
        print("Shutting down...")
    else :
        print("Choose again")