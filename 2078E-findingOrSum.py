# Author : AlifSrSE
# Date : 2025-03-15
# Problem link : https://codeforces.com/contest/2078/problem/E
 
def solve():
    n1 = 0
    print(n1)
    import sys
    sys.stdout.flush()
    res1 = int(input())
 
    n2 = 2**30 - 1
    print(n2)
    sys.stdout.flush()
    res2 = int(input())
 
    print("!")
    sys.stdout.flush()
    m = int(input())
 
    result = 0
    for i in range(30):
        bit_m = (m >> i) & 1
        bit_n1 = (n1 >> i) & 1
        bit_n2 = (n2 >> i) & 1
 
        if bit_m == 0:
            result += (res1 >> i) & 1
        else:
            if bit_n1 == 0 and bit_n2 == 1:
                result += (res2 >> i) & 1
            else:
                result += 1
 
    print(result)
    sys.stdout.flush()
 
t = int(input())
for _ in range(t):
    solve()