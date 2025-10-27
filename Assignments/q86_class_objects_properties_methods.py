class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hi, I'm {self.name}, and I'm {self.age} years old."

    def have_birthday(self):
        self.age += 1
        print(f"Happy birthday, {self.name}! You are now {self.age}.")

    def compare_age(self, other: "Person") -> str:
        if self.age > other.age:
            return f"{self.name} is older than {other.name}."
        elif self.age < other.age:
            return f"{self.name} is younger than {other.name}."
        else:
            return f"{self.name} and {other.name} are the same age."

if __name__ == "__main__":
    alice = Person("Alice", 30)
    bob = Person("Bob", 28)

    print(alice.greet())
    print(bob.greet())

    bob.have_birthday()
    print(alice.compare_age(bob))

print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")
