x = int(input("Enter x: "))
y = int(input("Enter y: "))
 
x = x ^ y
y = x ^ y
x = x ^ y
 
print("Value of x:", x)
print("Value of y:", y)