# watkins glen fudge co
# building a robot fudge crafter
import time
##
## cls
## fudge menu
menu0 = """Fudge\t\t$1.50 per ounce
Chocolates\t$1.50 per ounce
Coffee\t\t$2.00 per cup """
## Introductions
print("Hello, welcome to the watkins glen fudge company! My name is alan.")
name0 = input("What is the name for your order? ")
print("Hello " + name0 + ", what can i help you with today?\n")
print("Here is our menu:\n" + menu0)
## Asking for order
time.sleep(2)
print("\nWhat can I get for you today, " + name0 + "?" )
## Order collection and charge customer
order = input()
price0 = 1.50
price1 = 2.00
quantity = input("How many ounces/coffees would you like today? ")

total = price0 * int(quantity)

print("Okie dokie " + name0 + ". We will have your " + quantity + "x" + order + " ready momentarily!\n")
print("Your total today will be $" + str(total) + " USD.")

