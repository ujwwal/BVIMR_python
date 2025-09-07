# Q42. Slicing of the list.

if __name__ == "__main__":
    nums = list(range(10))  # [0..9]
    print("List:", nums)
    print("nums[2:7]:", nums[2:7])
    print("nums[:5]:", nums[:5])
    print("nums[5:]:", nums[5:])
    print("nums[::2]:", nums[::2])
    print("nums[1::2]:", nums[1::2])
    print("nums[-3:]:", nums[-3:])
    print("nums[::-1] (reversed):", nums[::-1])