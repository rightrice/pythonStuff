## loveseat
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Comes in Red or White. "
lovely_loveseat_price = 254.00
## settee
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Comes in ebony. "
stylish_settee_price = 180.50
## lamp
luxurious_lamp_description = "\nLuxurious Lamp. Glass and Iron. 36 inches tall. Brown with cream shade. "
luxurious_lamp_price = 52.15
## the taxman
sales_tax = 0.088
## first customer
customer_one_total = 0
customer_one_itemization = ""
## shopping cart
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description
## checkout
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax
## receipt
print("Customer One Items:")
print(customer_one_itemization)
print("\nCustomer One Total:")
print(customer_one_total)