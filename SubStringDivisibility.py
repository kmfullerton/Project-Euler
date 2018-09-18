from itertools import permutations
def generate_pandigitals(start_digit, end_digit):
    pandigital_list = []
    pandigital_list = list(permutations(range(start_digit, end_digit)))
    pandigital_list.sort()
    return pandigital_list

def main():
    sum = 0
    start_digit = 0
    end_digit = 10
    pandigital_list = generate_pandigitals(start_digit, end_digit)
    print('pandigital list:', pandigital_list)

    start_index = list([2, 3, 4, 5, 6, 7, 8])
    divisor_list = list([2, 3, 5, 7, 11, 13, 17, 23])

    for pan_num in pandigital_list:

        print('pan num:', pan_num)

        for i in len(range(0,start_index+1,1)):
            index = start_index[i]-1
            print('index:', i)
            divisor = divisor_list[index]
            print('divisor:', divisor)
            digit1 = str(pan_num[index])
            digit2 = str(pan_num[index + 1])
            digit3 = str(pan_num[index + 2])
            sub_str = ''.join([digit1, digit2, digit3])
            sub_num = int(sub_str)
            print('sub number: ', sub_num)
            if (sub_num%divisor == 0):
                sum += pan_num

    print('sum:', sum)



main()