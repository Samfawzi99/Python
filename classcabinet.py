#variables
answer = str()
num_drawers = int()
length = float()
width = float()
depth = float()
volume = float()
drawer_price = float()
total_drawer_price = float()
total_cabinet_price = float()
order_total = float()
#ask user if they want to build a cabinet
answer = input("Do you want to build a cabinet:  ")
#outer loop for order total
while answer == "yes":
    #ask for number of drawers
    num_drawers = int(input("Enter the number of drawers:   "))
    #inner loop to determine total drawer cost
    for counter in range (0, num_drawers):
        #ask for length, width and depth
        length = float(input("Enter the length:    "))
        width = float(input("Enter the width:    "))
        depth = float(input("Enter the depth:    "))
        #calculate the volume and drawer cost
        volume = length * width * depth
        drawer_price = volume * 0.05
        #output drawer price
        print("The cost of one drawer is:     ", drawer_price)
        #accumlating the drawers
        total_drawer_price = total_drawer_price + drawer_price
    #end for loop
    #calculate and output cabinet price
    total_cabinet_price = total_drawer_price + 100
    print("The cost for one cabinet is:  ", total_cabinet_price)
    total_drawer_price = 0
    order_total = order_total + total_cabinet_price
    #ask the user if they want to continue
    answer = input("Do you want to continue pricing cabinets:   ")
#end outer while loop
print("Total Order Cost:   ", order_total)