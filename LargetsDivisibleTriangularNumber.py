## Problem 12 from Project Euler.net
import numpy as np
import pandas as pd

def generate_triangle_numbers(tri_index):
    sum = 0
    for i in range(1,tri_index+1,1):
        sum = sum + i

    return sum

def find_all_factors(num):
    factors= []
    for i in list(range(1,num+1,1)):
        if num%i == 0: # Is this number a factor of the number in question?
            #print('Factor:', i)
            factors.append(i)

    return factors

def main():

    output = np.array([[0, 0, 0], [1, 1, 1]])
    num_fact = output[1,2]
    while num_fact < 500:
        #print(output)
        shape = output.shape
        num_rows = shape[0]-1
        #print('num rows:', num_rows)
        prev_sum = output[num_rows,1]
        #print('prev sum:', prev_sum)
        prev_index = output[num_rows,0]
        #print('prev index:', prev_index)
        new_index = prev_index +1
        new_sum = prev_sum + new_index

        factors = find_all_factors(new_sum)
        num_fact = len(factors)

        new_row = np.array([new_index, new_sum, num_fact])
        print('new row:', new_row)
        output = np.vstack([output, new_row])




main()