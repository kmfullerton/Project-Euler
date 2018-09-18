def main():
    min_val = 1
    max_val = 1000

    int_list = list(range(min_val, max_val+1,1))
    sum = 0
    for num in int_list:
        val = num ** num
        sum += val

    print('The sum is:', sum)

    digits = [int(x) for x in str(sum)]
    i = -1
    last_ten= []
    while i >= -11:
        digit = digits[i]
        last_ten.append(digit)
        i = i-1
    
    print('The last 10 digits are:', last_ten)
    print('actually 10 digits?', len(last_ten))

main()