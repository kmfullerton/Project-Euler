def main():
    min_val = 1
    max_val = 1001
    int_list = list(range(min_val, max_val, 1))
    perim_list = []
    for a in int_list:
        new_range = list(range(1, (max_val -a), 1))
        for b in new_range:
            c = 1000 - (a+b)
            perimeter = a + b + c
            perim_list.append(perimeter)

    l = perim_list

    perim_dict = dict((x, l.count(x)) for x in set(l))

    max_key = max(perim_dict, key=perim_dict.get)
    print('most frequent perimeter:', max_key)

main()
