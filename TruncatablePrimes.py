import isPrime

def truncate_l2r(num):
    digits = [x for x in str(num)]

    for i in len(digits):
        new_num_list = [i:]
        new_num = ''.join(new_num_list)
        if isPrime(new_num):
            print('truncated number:', new_num, ' is prime')
        else:
            return False

    return True

def truncate_r2l(num):
    digits = [x for x in str(num)]

    for i in len(digits):
        new_num_list = [-1:]
        new_num = ''.join(new_num_list)
        if isPrime(new_num):
            print('truncated number:', new_num, ' is prime')
        else:
            return False

    return True


def main():
    min_num = 10
    max_num = 5000
    sum = 0
    int_list = list(range(min_num, max_num, 1))

    for val in int_list:
        # Check if prime:
        if isPrime(in):
            # Truncate left to right
            l2r = truncate_l2r(val)
            if l2r:
                # Truncate right to left
                r2l = truncate_r2l(val)
                sum += val
    print('the sum is:', sum)

main()