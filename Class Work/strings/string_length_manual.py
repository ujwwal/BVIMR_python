# Program to check length of string without using inbuilt function

def string_length(s):
    count = 0
    for i in s:
        count += 1
    return count

# Example usage
input_str = input("Enter a string: ")
length = string_length(input_str)
print("Length of the string:", length)