# Author : AlifSrSE
# Date : 2025-03-10
# Problem link : https://codeforces.com/contest/158/problem/B

import math
def main():    
    n = int(input())
    ones = twos = threes = tx = 0
    arr = list(map(int, input().split()))
    
    for ai in arr:
        if ai == 4:
            tx += 1
        elif ai == 3:
            threes += 1
        elif ai == 2:
            twos += 1
        else:
            ones += 1
    
    if threes > ones:
        tx += threes
        tx += (twos // 2) + (twos % 2)
    elif threes < ones:
        tx += threes
        ones -= threes
        tx += (twos // 2)
        twos %= 2
        if twos:
            tx += 1
            ones -= 2
        if ones > 0:
            tx += ones // 4
            if ones % 4:
                tx += 1
    else: 
        tx += threes
        tx += (twos // 2) + (twos % 2)
    
    print(tx)

if __name__ == "__main__":
    main()