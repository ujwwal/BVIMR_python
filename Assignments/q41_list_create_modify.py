# Q41. Create and modify a list.

if __name__ == "__main__":
    nums = [1, 2, 3]
    print("Start:", nums)
    nums.append(4)
    nums.insert(1, 10)
    nums.extend([5, 6])
    print("After add:", nums)
    nums.remove(10)
    popped = nums.pop()  # remove last
    print("Removed last:", popped, "Now:", nums)
    nums[0] = 99
    print("After update:", nums)