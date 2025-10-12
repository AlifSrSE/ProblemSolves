# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

input = sys.stdin.read
data = input().split()
index = 0

t = int(data[index])
index += 1

for _ in range(t):
    n = int(data[index])
    index += 1
    k = int(data[index])
    index += 1
    s = data[index]
    index += 1
    forced = [-1] * k
    possible = True

    for i in range(n):
        if s[i] != '?':
            r = i % k
            val = int(s[i])
            if forced[r] == -1:
                forced[r] = val
            elif forced[r] != val:
                possible = False
                break
    if not possible:
        print("NO")
        continue
    fsum = 0
    num_free = 0

    for r in range(k):
        if forced[r] != -1:
            fsum += forced[r]
        else:
            num_free += 1
            
    target = k // 2
    if fsum <= target <= fsum + num_free:
        print("YES")
    else:
        print("NO")
