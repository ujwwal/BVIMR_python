# Q29. Calculate income tax per slabs (progressive).

def calculate_tax(income: float) -> float:
    slabs = [
        (250000, 0.00),
        (500000, 0.05),
        (1000000, 0.10),
        (2000000, 0.20),
        (3000000, 0.30),
        (float("inf"), 0.40),
    ]
    tax = 0.0
    prev = 0.0
    for upper, rate in slabs:
        taxable = max(0.0, min(income, upper) - prev)
        tax += taxable * rate
        prev = upper
        if income <= upper:
            break
    return tax


if __name__ == "__main__":
    income = float(input("Enter annual income (Rs.): "))
    tax = calculate_tax(income)
    print(f"Income: Rs. {income:,.2f}")
    print(f"Tax: Rs. {tax:,.2f}")

print("code written by ujjwal gupta - 0231bca051 of bca 5th sem bvimr")
