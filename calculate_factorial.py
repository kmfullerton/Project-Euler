def calculate_factorial(num):
    prod = 1

    for i in range(1, num, 1):
        prod = prod * i

    return prod