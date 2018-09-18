def check_pythagorean(a,b,c):
    if (a**2 + b**2) == c**2:
        print('Values ', a,', ', b, ', ', c, ' are a pythagorean triplet')
        return True
    else:
        return False

def check_sum(a,b,c):
    if a + b + c == 1000:
        print('Values ', a, ', ', b, ', ', c, ' sum to 1000')
        return True
    else:
        return False

def main():
    max_val = 1000
    avals = list(range(1,max_val,1))
    bvals = [aval + 1 for aval in avals]
    cvals = [bval + 1 for bval in bvals]

    for a in avals:
        for b in bvals:
            for c in cvals:
                if (a<b):
                    if (b<c):
                        if check_pythagorean(a,b,c): # The pythagorean triplet requirement is more stringent,
                            # and so is first
                            if check_sum(a,b,c): # The sum requirement is less stringent, and so is placed
                                # secondarily to minimize time

                                print('The triple is:', a, ',', b, ', ', c)
                                prod = a*b*c
                                print('The product is:', prod)
                                break

main()