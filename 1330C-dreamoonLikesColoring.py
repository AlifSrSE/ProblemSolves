# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

n, m = map(int, input().split())
l = list(map(int, input().split()))

if sum(l) < n:
    print(-1)
else:
    p = []
    last_covered = 0
    for i in range(m):
        max_start = n - l[i] + 1
        p_i = max(1, last_covered - l[i] + 1)
        if p_i > max_start:
            print(-1)
            exit()
        p.append(p_i)
        last_covered = max(last_covered, p_i + l[i] - 1)
    
    if last_covered < n:
        print(-1)
    else:
        print(*p)