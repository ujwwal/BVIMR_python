# Q25. Print pattern:
# *
# **
# ***
# ****
# *****
def print_pattern(n: int = 5) -> None:
    for i in range(1, n + 1):
        print("*" * i)


if __name__ == "__main__":
    # Change the number to print more/less rows
    print_pattern(5)