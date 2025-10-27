# Q48. Access and remove dictionary element.

if __name__ == "__main__":
    d = {"name": "Alice", "age": 30, "city": "Delhi"}
    print("name:", d["name"])
    print("age (get):", d.get("age"))
    removed = d.pop("city")
    print("Removed city:", removed, "Remaining:", d)
    del d["name"]
    print("After deleting name:", d)

print("This program is written by Ujjwal Gupta - 0231BCA051 of BCA 5th sem, BVIMR")
