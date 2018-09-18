def main():
    int_list = list(range(1, 101, 1))
    max_sum = 0
    for a in int_list:
        for b in int_list:
            sum = 0
            power = a**b
            digits = [int(x) for x in str(power)]

            for val in digits:
                sum += val

            if (sum >= max_sum):
                max_sum = sum
                print(a, ' to the ', b, 'power has a digit sum of ', sum)

main()