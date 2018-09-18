
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
    max_val = 999

    sum = sum_of_multiples(list_of_multiples, max_val)
    print('The sum of multiples is:', sum)

main()