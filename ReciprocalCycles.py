import numpy as np


def calc_reciprocal(num):

    recip = 1.0/float(num)

    return recip

def check_repeating(num, d):

    if (int(len(num)/d) <2):
        return False
    else:
        data = np.array(num)
        shape = (int(len(num)/d), int(d))
        data.reshape(shape)
        return True

def main():
    d = 10.0
    while d < 100.0:
        print('d', d)
        # Calculat the reciprocal
        recip = calc_reciprocal(d)
        print('recip:', recip)
        # Convert reciprocal to string and strip first portion
        recip = str(recip)
        recip = recip.strip('0.')
        # Convert digits into a list
        digits = [int(x) for x in str(recip)]
        # If there are more digits than d:
        print('length of digits:', len(digits))
        if len(digits) >= int(d):
            digits = np.reshape(digits, (-1,int(d-1)))
            col = 0
            while col < d:
                col_vals = digits[:,col]
                data = np.array(col_vals).tolist()
                unique_vals = set(data)
                if len(unique_vals) > 1:
                    print(d, 'is the number of interest')
                col += 1
            d += 1
        else: # if there are not more digits than d, move to the next number
            print('d', d, ' recip', recip)
            d += 1


main()