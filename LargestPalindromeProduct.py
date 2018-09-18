
def isPalindrome(num):
    digits = [int(i) for i in str(num)]
    #print(digits)
    flipped = digits[::-1]
    #print(flipped)
    if digits == flipped:
        return True
    else:
        return False

def main():
    min_num = 100
    max_num = 1000
    nums = list(range(min_num,max_num,1))
    palindromes = []
    for num1 in nums:
        for num2 in nums:
            prod = num1*num2
            if isPalindrome(prod):
                palindromes.append(prod)
    max_pal = max(palindromes)
    print('The largest palidnrome product between ', min_num, 'and ', max_num, 'is: ', max_pal)
    return max_pal




main()