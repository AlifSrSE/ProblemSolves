# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

n, k = map(int, input().split())
a = list(map(int, input().split()))

target = a[k-1]

possible = True
for num in a[k-1:]:
    if num != target:
        possible = False
        break

if not possible:
    print(-1)
else:
    operations = 0
    for i in range(k-2, -1, -1):
        if a[i] != target:
            operations = i + 1
            break
    print(operations)
