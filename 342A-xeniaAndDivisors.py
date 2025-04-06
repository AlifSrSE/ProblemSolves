# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

grouped_arr = [[0] * (n//3) for _ in range(3)]

for i in range(n//3):
    grouped_arr[0][i] = arr[i]
for i in range(n//3, (n//3)*2):
    grouped_arr[1][i - (n//3)] = arr[i]
for i in range((n//3)*2, n):
    grouped_arr[2][i - ((n//3)*2)] = arr[i]

all_good = True
for i in range(n//3):
    if (grouped_arr[0][i] >= grouped_arr[1][i] or 
        grouped_arr[1][i] >= grouped_arr[2][i]):
        all_good = False
    if (grouped_arr[1][i] % grouped_arr[0][i] != 0 or 
        grouped_arr[2][i] % grouped_arr[1][i] != 0):
        all_good = False

if all_good:
    for i in range(n//3):
        print(f"{grouped_arr[0][i]} {grouped_arr[1][i]} {grouped_arr[2][i]}")
else:
    print(-1)