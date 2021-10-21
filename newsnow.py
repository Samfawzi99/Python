#declare variables
#inchesFriday = int()
#inchesSaturday = int()


#Getting number of inches from user
inchesFriday = (str)
inchesSaturday =(str)
city = (str)
inchesFriday = input("Enter number of inches that fell on Friday:   ")
inchesSaturday = input("Enter number of inches that fell on Saturday:   ")
city = input("Enter the city where the snow fell:   ")
print




#Decomposition
#inputs: friday and satuday snow,city
#outputs: city and total
#process

#1. Get snow amounts and city from the user
#2. Add both days
#3. Output total and city to the user

#Algorithm
#1. Get friday snow amount
#2. Get satuday snow amount
#3. Get city
#4 Add two days of snow
#5. Output total snow fall
#6. Output city

#variables
friday_snow = float()
sat_snow = float()
total_snow = float()
city = str()
#Get inputs
city = input("Enter the city you live in:    ")
friday_snow = float(input("Enter Friday's snow amount:    "))
sat_snow = float(input("Enter Saturday's snow amount:   "))

#add snow amounts
total_snow = friday_snow + sat_snow

#outputs to the user
print("In", city, total_snow, "inches of snow fell.")
print("In " + city + " " + str(total_snow) + " inches of snow fell.")

