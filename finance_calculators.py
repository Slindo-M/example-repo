# This script allows the user to choose  a financial caluculator to use.
# It includes options for calculating simple interest, compound interest, and monthly payments on a loan.
import math
print("Investment - to calculate the amount of interest you'll earn on your investment.")

print("Bond - to calculate the amount you'll have to pay on a home loan.")

choice = input("Please choose either 'Investment' or 'Bond' from the menu above.")

# This script removes case sensitivity from the user's choice.
if choice.lower() == "investment":
    choice = "Investment"
elif choice.lower() == "bond":
    choice = "Bond"
else:
    print("You have not selected a valid option. Please try again.")
    exit(1)

if choice == "Investment":
    p = int(input("Please input the amount of money you are depositing."))
    r = float(input("Please input the interest rate as a percentage.")) / 100
    t = int(input("Please input the number of years you will be investing for."))
    simple = p * (1 + r * t)
    compound = p * math.pow((1 + r), t)
    type_of_interest = input("Please input either 'simple' or 'compound' to indicate the type of interest you want to calculate.")
    if type_of_interest == "simple":
        print("The amount of interest you'll earn on your investment is: R" + str(simple))
    else:
        print("The amount of interest you'll earn on your investment is: R" + str(compound))

else:
    p_v = float(input("Please input the present value of the house."))
    i = float(input("Please input the interest rate as a percentage.")) / 100 / 12
    n = int(input("Please input the number of months you will be paying the bond for."))
    bond_repayment = (i * p_v) / (1 - (1 + i) ** -n)
    print("The amount you'll have to pay on your home loan is: R" + str(bond_repayment))
