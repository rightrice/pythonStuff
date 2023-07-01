## rightrice
## CITA 180 
## Programming Assignment 01
##
import math
## Input
transaction = float(23.97)
print(f"Your total today is {transaction}.")
tendered = int(input("How much will you be tendering: $"))

## Processing
change = tendered - transaction
roundedChange = (math.ceil(change*100)/100)
## NOTE: i didn't use round because I didn't see it anywhere in zyBook, 
## however, using round to 2 places allowed for the correct change to be given.


## Output
print(f"Your change today is ${roundedChange}. Have a wonderful day!")
