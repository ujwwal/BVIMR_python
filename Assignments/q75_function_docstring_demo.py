def add(a, b):
    """
    Add two values and return the result.

    Uses Python's + operator, so it works for numbers, strings, lists, etc.

    Args:
        a: First value.
        b: Second value.

    Returns:
        The sum/concatenation of a and b.

    Examples:
        >>> add(2, 3)
        5
        >>> add(1.5, 2.5)
        4.0
        >>> add("py", "thon")
        'python'
        >>> add([1], [2, 3])
        [1, 2, 3]
    """
    return a + b


if __name__ == "__main__":
    print(add(2, 3))

print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")
