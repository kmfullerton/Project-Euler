def main():
    amin = 2
    amax = 100
    bmin = 2
    bmax = 100


    a = list(range(amin,amax+1,1))
    b = list(range(bmin,bmax+1,1))

    product = []
    for aval in a:
        for bval in b:
            prod = aval ** bval
            product.append(prod)

    ordered_products = sorted(product)

    unique_vals = set(ordered_products)

    num_terms = len(unique_vals)
    print(num_terms)

main()