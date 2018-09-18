def generate_fibonacci_sequence(max_val):
    list = [1,2]
    new_val = list[0] + list[1]
    while new_val < max_val-1:
        new_val = list[-1] + list[-2]
        print('Next Number in sequence:', new_val)
        list.append(new_val)
    return list

def select_only_evens(list):
    new_list = []
    for val in list:
        if val%2 == 0:
            new_list.append(val)

    return new_list

def sum_list(list):
    sum = 0
    for val in list:
        sum = sum + val

    return sum

def main():
    max_val = 4000000
    fib_seq = generate_fibonacci_sequence(max_val)
    even_fib_seq = select_only_evens(fib_seq)
    total_sum = sum_list(even_fib_seq)

    print('The sum of all even fibonacci numbers below', max_val, 'is:', total_sum)

main()