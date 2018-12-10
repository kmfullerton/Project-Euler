
def sum_of_multiples(list_of_multiples, max_val):
    sum = 0
    for mult in list_of_multiples:
        for i in range(1, max_val):
            if i%mult == 0:
                print("multiple of", mult, ":", i)
                sum = sum + i
                print(sum)
    return sum

def main():
    list_of_multiples = [3, 5]
    max_val = 9
    sum = 0


    for mult in list_of_multiples:
        print('multiplier:', mult)
        i = 1
        prod = mult * i
        while prod < max_val:
            prod = mult * i
            sum += prod
            print('The sum is:', sum)
            i = i+1

    print('The sum of multiples is:', sum)

main()