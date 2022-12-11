# parts list
# created by rightrice
from clickClack import clickClack as cc
from time import sleep

lan_party_stuff = "pc, cat8 ethernet cables, gaming chairs, tables, monitors, router, switch, snacks, drinks"
lan_list = ["pc", "cat8 ethernet cables", "gaming chairs", "desks", "monitors", "router", "switch","snacks", "drinks", "surge protector", "phone charger"]

##print(type(lan_list))
# specs order: cpu, gpu, ram, amount of ram, storage type, amount of storage (TB)
pc_specs = ["i9-12900KS", "ASUS TUF RTX 3080 OC 12GB", "Corsair Vengeance LPX", '32', "M.2 Drive Storage", '4']
cpu = pc_specs[0]
gpu = pc_specs[1]
ram = pc_specs[2]
ramAmount = pc_specs[3]
storageType = pc_specs[4]
storageAmount = pc_specs[5]

cc("Loading Module. . .")
cc("Please wait")
sleep(1)
cc("The CPU is: " + cpu)
cc("The GPU is: " + gpu)
cc("The RAM is: " + ram)
cc("The RAM storage is: " + ramAmount + "GB")
cc("The Storage Type is: " + storageType)
cc("The Amount of Storage is: " + storageAmount + "TB")
cc("\n\tthank you for using rightrice's list module")
cc("\n\t\t. . . goodbye")
