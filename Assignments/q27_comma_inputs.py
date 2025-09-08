# Q27. Multiple inputs, variable inputs and integer inputs separated by commas.

def read_two_ints_comma_separated():
    a_str, b_str = input("Enter two integers separated by commas (e.g., 10,20): ").split(",")
    a, b = int(a_str.strip()), int(b_str.strip())
    print(f"{a},{b}")  # comma-separated


def read_variable_ints_comma_separated():
    raw = input("Enter any number of integers (comma-separated): ")
    nums = [int(x.strip()) for x in raw.split(",") if x.strip()]
    print("List:", nums)
    print("Comma-separated:", ",".join(map(str, nums)))
    print("Count:", len(nums))


if __name__ == "__main__":
    read_two_ints_comma_separated()
    read_variable_ints_comma_separated()

print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")