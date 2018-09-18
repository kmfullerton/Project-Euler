def main():

    base_num = 2
    power = 1000

    large_num = base_num ** power

    digits = [int(x) for x in str(large_num)]

    sum = 0
    for digit in digits:
        sum = sum + digit

    print('Sum of the digits of ', base_num, ' to the ', power,' power is:', sum)


main()