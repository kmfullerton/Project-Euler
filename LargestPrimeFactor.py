def find_all_factors(num):
    prime_factors= []
    for i in range(1,num):
        if num%i == 0: # Is this number a factor of the number in question?
            print('Factor:', i)
            if isPrime(i) == True: # Is this factor a prime number?
                print('This factor is prime')
                prime_factors.append(i)
    print('The factors of ', num, 'are:', prime_factors)
    return prime_factors

# Note: this isPrime function is extremely slow- good candidate for optimization
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
    num = 600851475143
    prime_factors = find_all_factors(num)
    max_factor = max(prime_factors)
    print('The largest prime factor of', num, 'is:', max_factor)

main()