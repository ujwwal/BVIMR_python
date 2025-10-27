counter = 0  # Global variable

def increment():
    global counter
    counter += 1
    print("increment() -> counter:", counter)

def read_only():
    print("read_only() sees counter:", counter)

if __name__ == "__main__":
    print("Initial counter:", counter)
    increment()
    increment()
    read_only()