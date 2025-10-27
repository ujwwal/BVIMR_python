counter = 0  # Global

def outer():
    global counter
    counter += 1

    message = "hello"  # enclosing scope

    def inner():
        nonlocal message
        global counter
        message += " world"
        counter += 1
        print("inner -> message:", message, "| counter:", counter)

    print("outer before inner -> message:", message, "| counter:", counter)
    inner()
    print("outer after inner -> message:", message, "| counter:", counter)

if __name__ == "__main__":
    print("Initial counter:", counter)
    outer()
    print("Final counter:", counter)

print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")
