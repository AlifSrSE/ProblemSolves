# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    line = input().strip()
    if ' ' in line:
        A, B = line.split()
    else:
        A = line
        B = input().strip()
    
    n = len(A)
    c = [0, 0]
    
    for i in range(n):
        c[int(A[i])] += 1
        c[int(B[i])] -= 1
    
    if c[0] != 0 or c[1] != 0:
        print(-1)
        return
    
    ans = 0
    A = list(A)
    
    if A[0] != B[0]:
        c = A[0]
        one = 0
        while one < n and A[one] == A[0]:
            one += 1
        two = one
        while two < n and A[two] == A[one]:
            two += 1
        bound = two - one
        for i in range(two):
            if i < bound:
                A[i] = str(int(c) ^ 1)
            else:
                A[i] = c
        ans += 1
    
    if A[-1] != B[-1]:
        c = A[n-1]
        one = n-1
        while one >= 0 and A[one] == A[n-1]:
            one -= 1
        two = one
        while two >= 0 and A[two] == A[one]:
            two -= 1
        bound = one - two
        j = 0
        for i in range(n-1, two, -1):
            if j < bound:
                A[i] = str(int(c) ^ 1)
            else:
                A[i] = c
            j += 1
        ans += 1
    
    blockA = []
    blockB = []
    
    i = 0
    while i < n:
        j = i
        while j < n and A[j] == A[i]:
            j += 1
        blockA.append(j - i)
        i = j
    
    i = 0
    while i < n:
        j = i
        while j < n and B[j] == B[i]:
            j += 1
        blockB.append(j - i)
        i = j
    
    blockA.reverse()
    blockB.reverse()
    
    while blockA:
        if len(blockA) < len(blockB):
            ans = -1
            break
        if blockA[-1] == blockB[-1]:
            blockA.pop()
            blockB.pop()
            continue
        if blockA[-1] > blockB[-1]:
            ans = -1
            break
        if len(blockA) < 4:
            ans = -1
            break
        x = blockA.pop()
        y = blockA.pop()
        blockA[-1] += x
        blockA[-2] += y
        ans += 1
    
    print(ans)

t = int(input())
for _ in range(t):
    solve()