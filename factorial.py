factorial_num = int(input("Enter a number:"))
if( factorial_num < 0):
    print("Factorial is not defined for negative numbers.")

result=1
for i in range(1,factorial_num+1):
    result*=i
print("factorial of ",factorial_num,'is',result)
