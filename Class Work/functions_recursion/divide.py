def divideNos(num,deno):
    """
    divide two numbers and return the result.

    Parameters:
    num(float): the num of the division
    deno(float): the deno of the division. must not be zero

    Returns:
    float:the result of division

    Raises:
    ValueError: if the deno is zero.
    """

    if deno  == 0:
        raise ValueError ("deno must not be zero")
    return num/deno

a = divideNos(11,23)

print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")