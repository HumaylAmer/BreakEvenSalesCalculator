#wage = 15
#hours = 40
#weeks = 48
#salary = wage * hours * weeks
#print('The Salary for this person is:', salary)

#My own break even ppoint calculator
print("In Business the Break Even Point is the level of sales at which the total fixed and variable costs of a business becomes equal to its revenue, thus leading to no profits or losses\n")
print("Your Fixed Costs (FC) are costs that remain the same and don't alter based on the number of sales, for example: rent, utility bills, equipment, etc\n")
print("Your Variable Costs (VC) are the costs that vary depending on the number of sold units, for example: packaging costs, delivery fees, etc.\n")

Fixed_Costs = float(input('What are your Fixed Costs? '))
Variable_Costs = float(input('What are your Variable Costs per unit? '))
Price_Per_Unit = float(input('What is the Price Per Unit? '))
Break_Even_Sales = (Fixed_Costs) / (Price_Per_Unit - Variable_Costs)
print('The minimum number of unit sales you have to achieve to net 0 is: ', Break_Even_Sales)






# Calculate the break-even point (in units) for T-Z
#break_even = fixed_costs/(sales_price - variable_costs_per_unit)

# Print the break even point in units
#print("The break even point is {} units.".format(break_even))

# Forecast the gross profit for January and February
#gross_profit_jan = (sales_price*units_jan) - cogs_jan
#gross_profit_feb = (sales_price*units_feb) - cogs_feb

# Print the gross profit for January and February
# print("The gross profit for January and February are {} and {} USD respectively.".format(gross_profit_jan, gross_profit_feb))