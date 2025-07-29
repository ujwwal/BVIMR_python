user_input = input("Enter a list of numbers seperated by spaced")

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

