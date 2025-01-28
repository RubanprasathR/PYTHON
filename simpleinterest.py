principal_amount = int(input("Enter the principal amount:"))
rate = int(input("Enter the rate of interest:")) 
time = int(input("Enter the time period:"))

result = (principal_amount*rate*time)/100
print("The simple interest is",result)
