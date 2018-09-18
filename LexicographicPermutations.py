from itertools import permutations

def create_permutation_list(digit_list):
    perm_list = permutations(digit_list)

    return perm_list



def main():
    min_val = 0
    max_val = 9
    digit_list = list(range(min_val, max_val+1, 1))

    perm_list = create_permutation_list(digit_list)

    sorted_list = sorted(perm_list)
    #print('sorted list:', sorted_list)

    index_of_interest = 1000000
    ans = sorted_list[index_of_interest-1]
    print(sorted_list[0:15])
    print('Permutation  ', index_of_interest, '  of the digits between ', min_val, ' and ', max_val, ' is: ', ans)

main()