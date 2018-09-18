def sum_digits(num):
    digits = [int(x) for x in str(num)]
    sum = 0
    for i in digits:
        sum = sum + i

    return sum