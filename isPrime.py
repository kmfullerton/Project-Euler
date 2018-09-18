def isPrime(num):
    if num >= 2:
        for n in range(2, num):
            if (num % n) == 0:
                return False
        # after the complete for n loop
        return True
    else:
        return False