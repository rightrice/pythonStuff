# Specc's Fudge
# building a robot fudge artisan
import time
##
## cls
## fudge menu
menu0 = """Fudge\t\t\t$1.50 per ounce
Chocolates\t\t$1.50 per ounce
Chocolate Beauties\t$1.75 per ounce
+++
Coffee\t\t\t$2.00 per cup
Italian Machiatto\t$3.75 per cup """
## introductions
print("Hello, welcome to Specc's Fudge! My name is alan.")
name0 = input("What is the name for your order? ")
## fudge bouncer
if name0 == "hulb":
    evil_status = input("\tAre you bad at VALORANT?\n")
    if evil_status == "yes":
        print("\tYou're not welcome back at Specc's Fudge, " + name0 + ". LEAVE!")
        exit()
    else:
        print("oh, dope. so you're radiant then? ")
else:
    print("Hello " + name0 + ", what can i help you with today?\n")
## fudge bouncer approved
print("Here is our menu:\n" + menu0)
## Asking for order
time.sleep(2)
print("\nWhat can I get for you today, " + name0 + "?" )
## Order collection and charge customer

order = input()
if order == "Coffee":
    price = 2.00
elif order == "Italian Machiatto":
    price = 3.75
elif order == "Chocolates":
    price = 1.50
elif order == "Fudge":
    price = 1.50
elif order == "Chocolate Beauties":
    price = 1.75
else:
    print("Oops, it doesn't seem like thats available at this time, please try again.")
    price = 0
quantity = input("How much would you like today? ")
tax = 1.08
total = price * int(quantity)
totalTax = total * tax

print("Okie dokie " + name0 + ". We will have your " + quantity + "x" + order + "(s)" + " ready momentarily!\n")
print("Your subtotal today will be $" + str(total) + " USD.")
print("Your total including tax will be $" + str(totalTax) + " USD.")