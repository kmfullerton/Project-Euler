def sum_squares(max_num):
    sum_of_squares = 0
    for i in range(1,max_num,1):
        sum_of_squares += i**2

    return sum_of_squares

def square_sums(max_num):
    sum = 0
    for i in range(1,max_num,1):
        sum += i
    square_of_sums = sum**2
    return square_of_sums

def main():
    max_num = 101
    sum_of_squares = sum_squares(max_num)
    print('sum of squares:', sum_of_squares)
    square_of_sums = square_sums(max_num)
    print('square of sums:', square_of_sums)
    diff = square_of_sums - sum_of_squares
    print('the difference is:', diff)

main()