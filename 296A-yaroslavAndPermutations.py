# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

n = int(input())
a = list(map(int, input().split()))
if n == 1:
    print("YES")
else:
    freq = {}
    for num in a:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    max_freq = max(freq.values())
    if max_freq > (n + 1) // 2:
        print("NO")
    else:
        print("YES")