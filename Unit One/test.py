user_input = input("Enter a list of numbers seperated by spaces: \n")

#conveert the input string to a list of strings
input_list = user_input.split()

#conveert the input string to a list of integers
numbers= list(map(int,input_list))

#step2 calculate sum of list
total = sum(numbers)

#step3 find length
length = len(numbers)

#sort the list
sorted_numbers = sorted(numbers)

#outputs
print(f"original list: {numbers}")
print(f"sum of numbers: {total}")
print(f"number of elements: {length}")
print(f"sorted lsit of numbers {sorted_numbers}")