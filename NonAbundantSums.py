def factor_sum(num):
    sum = 0
    for i in range(1,num):
        if num%i == 0: # Is this number a factor of the number in question?
            sum += i

    return sum

def is_proper(num):

    factors = find_all_factors(num)
    fact_sum = sum(factors)

    if fact_sum > num:
        type = 'Abundant'
    elif fact_sum < num:
        type = 'Deficient'
    else:
        type = 'Perfect'

    return type


def main():
    # Section 1: Classify each integer as deficient, perfect, or abundant
    min_val = 1
    max_val = 28123
    int_list = list(range(min_val, max_val, 1))
    dict_list = []
    abundant_list = list()
    deficient_list = list()
    perfect_list = list()
    for int in int_list:
        fact_sum = factor_sum(int)


        if fact_sum > int:
            abundant_list.append(int)
        elif fact_sum < int:
            deficient_list.append(int)
        else:
            perfect_list.append(int)

    # Section 2: Find all possible abundant sums
    abundant_sum_list = list()
    for num in abundant_list:
        sum = 0
        for num2 in abundant_list:
            sum = num + num2
            abundant_sum_list.append(sum)

    # remove duplicate values and truncate list
    all_abundant_sums = list(set(abundant_sum_list))
    all_abundant_sums = all_abundant_sums[:max_val]

    # Calculate total sum
    non_abundant_sum = 0
    for num in int_list:
        if num not in all_abundant_sums:
            non_abundant_sum += num


    print('The sum of all non abundant numbers between', min_val, ' and ', max_val, ' is:', non_abundant_sum)


main()