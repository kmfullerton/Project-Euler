
def convert_dec_to_binary(num):
    bin_num = bin(num)
    return bin_num[2:]

def check_palindrome(num):
    #print('num:', num)
    # convert number into digits
    digits = [x for x in str(num)]
   # print('digits:', digits)
    # reverse digits string
    reversed_list = digits[::-1]
    #print('reversed list:', reversed_list)
    reverse_str = ''.join(reversed_list)
    reversed_num = int(reverse_str)
    #print('reversed num:', reversed_num)
    # compare initial and reversed numbers
    if int(num) == reversed_num:
        return True
    else:
        return False


def main():
    sum = 0
    min_val = 0
    max_val = 1000001
    nums = list(range(min_val, max_val, 1))

    for num in nums:

        original_is_palindrome = check_palindrome(num)
        if original_is_palindrome:
           # print('original number:', num)
            binary = convert_dec_to_binary(num)
            #print('binary number:', binary)

            binary_is_palindrome= check_palindrome(binary)
            #print('binary is plaindrome?', binary_is_palindrome)

            if binary_is_palindrome:
                print('number:', num)
                print('binary:', binary)
                print('Binary is a palindrome as well!')
                sum += num
                #print('sum:', sum)
    print("The sum is:", sum)
main()