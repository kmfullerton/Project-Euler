

def check_divisors(min_divise, max_devise, num):
    divisor_list = list(range(min_divise, max_devise,1))
    multiple_list = []
    for int in divisor_list:
        if num%int == 0:
            # num is a multiple of int
            multiple_list.append(int)
    return multiple_list

def main():
    min_val = 100000000
    max_val = 1000000000
    min_mult = 1
    max_mult = 20
    dividend = list(range(min_val, max_val, 1))
    output = []
    divisor_list = list(range(min_mult, max_mult, 1))
    for num in dividend:
        multiple_list = []
        for int in divisor_list:
            if num % int == 0:
                # num is a multiple of int
                multiple_list.append(int)
            num_multiples = len(multiple_list)
        output.append([num, num_multiples])
        if num_multiples == max_mult:
            print(num, ' has ', num_multiples, ' multiples')
            break

    print('No number found between ', min_val, ' and ', max_val, ' that is divisible by all numbers between '
                                                                         '', min_mult, ' and ', max_mult)
main()
