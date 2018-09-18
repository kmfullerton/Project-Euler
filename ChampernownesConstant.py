def champernowne(num_digits):
    answer = ""
    c = 1
    for c in range(num_digits):
        answer += str(c)
    return answer

def main():
    num_digits = 1000001
    num = champernowne(num_digits)
    prod = 1
    i = 0
    while i <= 6:
        prod = prod * int(num[10**i])
        i += 1

    print('product:', prod)
main()