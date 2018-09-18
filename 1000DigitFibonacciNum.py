def generate_fibonacci_sequence(length):

    fibonacci_list = [1, 1]

    for int in list(range(2,length,1)):
        fnm1 = fibonacci_list[int-1]
        fnm2 = fibonacci_list[int-2]
        new_num = fnm1 + fnm2

        fibonacci_list.append(new_num)

    return fibonacci_list

def how_many_digits(num):
    digits = [int(x) for x in str(num)]
    num_digits = len(digits)
    return num_digits

def main():
    length = 10000

    fibonacci_seq = generate_fibonacci_sequence(length)
    num_digits = 1
    counter = 0
    while num_digits < 1000:
        num = fibonacci_seq[counter]
        num_digits = how_many_digits(num)
        counter += 1

    print('The number ', num, ' is the ', counter, ' fibonacci number and has ', num_digits, 'digits')

main()