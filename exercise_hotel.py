#declare variables
room_type = str()
month = str()
days = int()
room_price = float()
total_cost = float()
#1. ask the user for room type, month and days
print("Select a room type")
print("\tS\t=\tSingle")
print("\tD\t=\tDouble")
print("\tC\t=\tCondo")
room_type = input("Enter your choice:   ")
month = input("Enter the month you are traveling in:  ")
days = int(input("Enter the amount of days you are travling:  "))

#convert all string input to lower case
room_type = room_type.lower()
month = month.lower()

#2. determine the price per room

##single
##         may = 75
##         june = 85
##         july = 100
##         august = 105
##double
##         may = 95
##         june = 110
##         july = 125
##         august = 130
##condo
##         may = 125
##         june = 130
##         july = 150
##         august = 155


if room_type == "s":
    if month == "may":
        room_price = 75
    elif month == "june":
        room_price = 85
    elif month == "july":
        room_price = 100
    else:
        room_price = 105
    #endif
elif room_type == "d":
    if month == "may":
        room_price = 95
    elif month == "june":
        room_price = 110
    elif month == "july":
        room_price = 125
    else:
        room_price = 130
    #endif
elif room_type == "c":
    if month == "may":
        room_price = 125
    elif month == "june":
        room_price = 130
    elif month == "july":
        room_price = 150
    else:
        room_price = 155
    #endif

##3. calculate the total
##   total = room_price * days
total_cost = room_price * days

#4. output price per room and total
print("Room Cost:\t$", room_price)
print("Total Cost:\t$", total_cost)
        
