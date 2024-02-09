print("Restaurant Bill Generator ...", "\n")
#Restaurant bill generator wording

food = float(input("Please enter cost of food: "))
drinks = float(input("Please enter cost of drinks: "))
total = food + drinks
tax = 0.075
tip= 0.18
#variables

print("\n", "Restaurant Bill")
print("-----------------------------")
#restaurant bill wording and dashes under

tax_amount = round(total * tax, 2)
tip_amount = round((total + tax_amount) * tip, 2)
total_2 = round((total + tax_amount + tip_amount), 2)
#variables of for tax, tip, total_2

print("\n", "Cost of meal:   $", total)
print("Tax Amount:     $", tax_amount)
print("Tip Amount:     $", tip_amount)
print("                -------------")
#meal cost, tax, tip, dashes underneath

print("Total:          $", total_2)
#total printed
