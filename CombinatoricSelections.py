from math import factorial
from collections import Counter
def main():

    # Calculate number of combinations

    nvals = list(range(1, 101, 1))
    Clist = []
    for n in nvals:
        rvals = list(range(1, n+1, 1))
        for r in rvals:
            b = n-r
            C = factorial(n) / (factorial(r)*(factorial(b)))
            if C >= 1000000:
                Clist.append(C)
        #print('final r value:', r)


    Clist.sort()
    ans = len(Clist)

    print(ans)

main()