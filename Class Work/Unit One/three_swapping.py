#swapping 3 nos
a=10
b=15
c=20

a,b,c=c,a,b

#swapping using temp
temp = a
a = b
b = c
c = temp
print(a, b, c)

#math
a = a + b + c
b = a - (b + c)
c = a - (b + c)
a = a - (b + c)
