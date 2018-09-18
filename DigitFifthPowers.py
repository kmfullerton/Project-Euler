def main():
    power = 5

    int_list = list(range(2,10000001,1))
    outer_sum = 0
    for num in int_list:

        # Break each integer into digits
        digits = [int(x) for x in str(num)]

        # Find the sum of the powers of the digits
        sum = 0
        for digit in digits:
            sum += digit ** power

        # Check if the sum = the integer
        if sum == num:
            print(num, ' can be written as the sum of its digits to the ', power, 'power')
            outer_sum += num

    print('The final sum of all these numbers is: ', outer_sum)

main()