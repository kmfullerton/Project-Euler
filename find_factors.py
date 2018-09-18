def find_prime_factors(num):
    prime_factors= []
    for i in range(1,num):
        if num%i == 0: # Is this number a factor of the number in question?
            print('Factor:', i)
            if isPrime(i) == True: # Is this factor a prime number?
                print('This factor is prime')
                prime_factors.append(i)
    print('The factors of ', num, 'are:', prime_factors)
    return prime_factors

def find_all_factors(num):
    factors= []
    for i in range(1,num):
        if num%i == 0: # Is this number a factor of the number in question?
                factors.append(i)
    print('The factors of ', num, 'are:', factors)
    return factors