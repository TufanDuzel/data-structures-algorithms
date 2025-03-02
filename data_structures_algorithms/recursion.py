def calculate_factorial(num):
    # Edge case - Exit Condition.
    if num == 0:
        return 1
    else:
        return num * calculate_factorial(num - 1)
    
print(calculate_factorial(7))


def sequential_addition(num):
    # Edge case - Exit Condition.
    if num == 0:
        return 0
    else:
        return num + sequential_addition(num - 1)
    
print(sequential_addition(7))