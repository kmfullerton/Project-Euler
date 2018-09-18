import io
import pandas as pd
import string
import collections

def calc_name_val(name):
    # separate string into letters
    name_letters = [str(x) for x in str(name)]

    # Create dictionary
    letters = sorted(string.ascii_uppercase)
    d = dict(zip(letters, list(range(1, len(letters)+1, 1))))
    # Calculate name value
    sum = 0
    for l in name_letters:
        letter_val = d[l]
        sum = sum + letter_val

    return sum

def main():

    # Section 1: Open file and read names to dataframe
    file_name = 'names.txt'
    names = pd.read_csv(file_name)
    sorted_names = sorted(names)
    array = []
    counter = 1
    score_sum = 0
    for name in sorted_names:
        sum = calc_name_val(name)
        score = sum * counter
        score_sum += score
        counter += 1

    print('score sum:', score_sum)

main()