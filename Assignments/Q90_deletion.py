class Example:
    def __init__(self, name):
        self.name = name
        print(f"Object {self.name} created")
    
    def __del__(self):
        print(f"Object {self.name} deleted")

obj = Example("Test")
del obj  # Explicit deletion
# Output: Object Test created
#         Object Test deleted

print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")
