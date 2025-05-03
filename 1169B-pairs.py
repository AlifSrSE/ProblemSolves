# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1169/problem/B

def alif(n, a, b):
    m = len(a)
    
    for v1 in [a[0], b[0]]:
        index = None
        for i in range(m):
            if a[i] != v1 and b[i] != v1:
                index = i
                break

        if index is None:
            return True

        for v2 in [a[index], b[index]]:
            if all(a[i] == v1 or a[i] == v2 or b[i] == v1 or b[i] == v2 for i in range(m)):
                return True
    
    return False

n, m = map(int, input().split())
a = []
b = []
for _ in range(m):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
print("YES" if alif(n, a, b) else "NO")