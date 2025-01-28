value = int(input("Enter the number:"))
s=value
b = len(str(value))
sum=0
while value > 0:
    result = value % 10
    value = value // 10
    sum = sum +  (result**b)
    
    
if sum == s:
    print(sum,"is armstrong number")
else:
    print(sum,"is not armstrong number") 
