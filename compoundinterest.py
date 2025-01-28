principal_amount = int(input("Enter the principal amount:"))
rate = float(input("Enter the rate of interest:")) 
time = float(input("Enter the time period:"))

amount = principal_amount*(1+rate/100)**time
compound_interest = amount - principal_amount

print("compound interest is",compound_interest)
