def greet(name = "greet"):
    print(f"hello, {name}")

greet()
greet("alice")

def getUserinfo():
    name = "alice"
    age = 30
    return name,age

userName,userAge = getUserinfo()
print(userName)
print(userAge)