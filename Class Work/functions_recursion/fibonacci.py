def fibionaci(num):
    a, b = 0, 1
    for i in range(num):
        print(a, end=' ')
        a, b = b, a + b

def recFibionaci(num):
    if num <= 1:
        return num
    else:
        return recFibionaci(num - 1) + recFibionaci(num - 2)