#If the bill was $150.00, split between 5 people, with 12% tip. 
amt = float(input("Enter the Amount?\n"))
n = int(input("How many people\n"))
tip = int(input("Tip Percentage?\n"))
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
bill = (amt/n)*(1+tip/100)
rbill = format(bill, '.2f')#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# rbill = round(bill,2)
#Write your code below this line 👇
print(rbill)