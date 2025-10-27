if __name__ == "__main__":
    try:
        import q81_custom_module_myutils as myutils
        print("[Using custom module q81_custom_module_myutils]")
        print("is_prime(31):", myutils.is_prime(31))
        print("gcd(42, 56):", myutils.gcd(42, 56))
        print("lcm(5, 7):", myutils.lcm(5, 7))
        print("mean([10, 20, 30]):", myutils.mean([10, 20, 30]))
        print(myutils.greet("Bob"))
    except ModuleNotFoundError:
        import math
        print("[Custom module not found. Using built-in 'math' module instead]")
        print("sqrt(81):", math.sqrt(81))
        print("factorial(6):", math.factorial(6))
        print("gcd(42, 56):", math.gcd(42, 56))
        print("ceil(3.14):", math.ceil(3.14))