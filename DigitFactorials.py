import math
def main():

    int_list = list(range(3,1000001,1))
    outer_sum = 0
    for num in int_list:

        # split number into digits
        digits = [int(x) for x in str(num)]

        # find factorial of each digit
        sum = 0
        for digit in digits:
            fact = math.factorial(digit)
            sum += fact

        # check if sum = num
        if sum == num:
            print(num, ' can be written as the sum of the factorial of its digits')
            outer_sum += num

    print('the final sum is:', outer_sum)

main()