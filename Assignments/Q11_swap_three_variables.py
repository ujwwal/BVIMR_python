# Q11. Swap value of three variables using all possible ways

x, y, z = 1, 2, 3
print("Before swap: x =", x, ", y =", y, ", z =", z)

# Method 1: Using temp
temp = x
x = y
y = z
z = temp
print("After swap using temp: x =", x, ", y =", y, ", z =", z)

# Method 2: Using tuple unpacking
x, y, z = y, z, x
print("After swap using tuple unpacking: x =", x, ", y =", y, ", z =", z)

print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")