weight = input("How much does your package weigh?")
groundShip_cost = 0
premoGround = 125
droneShip_cost = 0
# Ground Shipping Pricing
if weight <= 2:
    groundShip_cost = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
    groundShip_cost = weight * 3 + 20
elif weight > 6 and weight <= 10:
    groundShip_cost = weight * 4 + 20
else:
    groundShip_cost = weight * 4.75 + 20

# Drone Shipping
if weight <= 2:
    droneShip_cost = weight * 4.5
elif weight > 2 and weight <= 6:
    droneShip_cost = weight * 9
elif weight > 6 and weight <= 10:
    droneShip_cost = weight * 12
else:
    droneShip_cost = weight * 14.25

print("Your ground shipping charge is: $", groundShip_cost)
print("Premium Ground Shipping: $", premoGround)
print("Drone Shipping: $", droneShip_cost)