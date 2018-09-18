def calculate_factorial(num):
    prod = 1

    for i in range(1, num, 1):
        prod = prod * i

    return prod

def sum_digits(num):
    digits = [int(x) for x in str(num)]
    sum = 0
    for i in digits:
        sum = sum + i

    return sum

def main():
    num = 100

    factorial = calculate_factorial(num)
    digit_sum = sum_digits(factorial)

    print(num, ' factorial is:', factorial)
    print('The sum of these digits is:', digit_sum)

main()