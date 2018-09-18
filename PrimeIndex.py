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
    i = 1
    index_of_interest = 10001
    prime_list = []
    while len(prime_list) <= index_of_interest:
        if isPrime(i):
            prime_list.append(i)
            i += 1
            print('Prime number:', i)
        else:
            i += 1

    print(prime_list)

    nth_prime = prime_list[index_of_interest-1]

    print('the ', index_of_interest, ' prime number is:', nth_prime)
main()