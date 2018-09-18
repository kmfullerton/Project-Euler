## Problem 11 from Project Euler.net
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
    max_val = 2000000
    sum = 0
    for i in range(1,max_val):
        if isPrime(i):
            print('Prime number:', i)
            sum = sum + i

    print('Sum of primes: ', sum)
    return sum

main()