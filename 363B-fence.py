# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

n, k = map(int, input().split())
h = list(map(int, input().split()))
current_sum = sum(h[:k])
min_sum = current_sum
min_index = 0

for i in range(1, n - k + 1):
    current_sum = current_sum - h[i - 1] + h[i + k - 1]
    if current_sum < min_sum:
        min_sum = current_sum
        min_index = i

print(min_index + 1)