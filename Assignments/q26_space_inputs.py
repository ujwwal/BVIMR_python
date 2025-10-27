# Q26. Multiple inputs, variable inputs and integer inputs separated by spaces.

def read_two_ints_space_separated():
    a, b = map(int, input("Enter two integers separated by spaces: ").split())
    print(a, b)  # space-separated by default


def read_variable_ints_space_separated():
    nums = list(map(int, input("Enter any number of integers (space-separated): ").split()))
    print(*nums)  # prints space-separated
    print("Count:", len(nums))


if __name__ == "__main__":
    read_two_ints_space_separated()
    read_variable_ints_space_separated()\

print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")

print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")
