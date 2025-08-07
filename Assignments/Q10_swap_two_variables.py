# Q10. Swap value of two variables using all possible ways

a, b = 5, 10
print("Before swap: a =", a, ", b =", b)

# Method 1: Using temp
temp = a
a = b
b = temp
print("After swap using temp: a =", a, ", b =", b)

# Method 2: Using tuple unpacking
a, b = b, a
print("After swap using tuple unpacking: a =", a, ", b =", b)

# Method 3: Using arithmetic
a = a + b
b = a - b
a = a - b
print("After swap using arithmetic: a =", a, ", b =", b)

# Method 4: Using XOR
a = a ^ b
b = a ^ b
a = a ^ b
print("After swap using XOR: a =", a, ", b =", b)

print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")