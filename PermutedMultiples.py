
def main():
    min_val = 1000
    max_val = 1000000
    multipliers = list(range(1, 7, 1))
    xlist = list(range(min_val, max_val, 1))
    for x in xlist:
        # Calculate the multiples of the candidate x:

        multiple_list = []
        for mult in multipliers:
            prod = x*mult
            digits = [int(x) for x in str(prod)]
            digits.sort()
            val = "".join(str(x) for x in digits)
            multiple_list.append(val)

        # print('multiple list:', multiple_list)


        if len(set(multiple_list)) == 1:
            print('x:', x)
            print('result set:', multiple_list)


main()