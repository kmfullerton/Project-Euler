import numpy as np

def find_all_factors(num):
    factors= []
    for i in range(1,num):
        if num%i == 0: # Is this number a factor of the number in question?
            factors.append(i)
    return factors

def calculate_sum_of_divisors(num):

    factors = find_all_factors(num)
    sum = 0
    for fact in factors:
        sum = sum + fact
    return sum

def find_amicable_nums(array):
    amicable = []
    rows = len(array)

    indicies = list(range(0,rows, 1))
    for i in indicies:
        b = array[i][1]
        if b <= rows:
            a = array[b][0]
        else:
            a = 0

        if a == b:
            amicable.append([a, b])

    return amicable

def main():
    output = []
    check_output = []
    for num in range(1,100000,1):
        a = num
        b = calculate_sum_of_divisors(a)
        output.append([a,b])
    print('output:', output)
    print('sample:', output[17][1])
    amicable_nums = find_amicable_nums(output)

    print('amicable set:',amicable_nums)


main()
