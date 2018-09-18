import numpy as np

def generate_sequence(start_num):
    seq = [start_num]
    num = start_num
    while num > 1:
        if num%2 == 0:
            #The number is even
            num = num/2
        else:
            num = (3*num) + 1
        seq.append(num)

    return seq

def main():

    max_length = 1
    max_num = 1
    start_nums = range(1,1000000,1)
    for start_num in start_nums:

        seq = generate_sequence(start_num)
        length = len(seq)
        if length > max_length:
            max_length = length
            max_num = start_num





    print('Starting with ', max_num, ' generates a sequence that is ', max_length, ' digits long')

main()