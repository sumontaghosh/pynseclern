x = 5
y = 7
 
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)

x, y = y, x
 
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)



x = 5
y = 10

print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)

x = x + y
y = x - y
x = x - y

print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)