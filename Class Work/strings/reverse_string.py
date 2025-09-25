def stringReversal(str):
    reversed_str = ""
    for char in str:
        reversed_str = char + reversed_str
    return reversed_str

talk = "hi"
print(stringReversal(talk))