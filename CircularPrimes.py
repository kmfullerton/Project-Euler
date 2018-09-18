
from itertools import permutations
def isPrime(num):
    if num >= 2:
        for n in range(2, num):
            if (num % n) == 0:
                return False
        # after the complete for n loop
        return True
    else:
        return False

def main():
    max_val = 10
    int_list = list(range(2,max_val+1, 1))
    circular_prime_list = []
    # check if number is prime
    for num in int_list:
        if isPrime(num):
            # split num into digits
            digits = [int(x) for x in str(num)]
            # calculate all the permuations
            perms = list(permutations(digits))
            for i in list(range(0,len(perms),1))
    #         # check if all permutations are prime
    #         for val in perms:
    #             if isPrime(val):
    #                 circular_prime_list.append(num)
    #
    # ans = len(circular_prime_list)
    # print('the circular primes are:', circular_prime_list)
    # print('the ans is:', ans)

main()