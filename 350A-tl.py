# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

min_wrong = min(b)
max_correct = max(a)
min_extra = min(a) * 2

lower_bound = max(max_correct, min_extra)
upper_bound = min_wrong - 1

if lower_bound <= upper_bound:
    print(lower_bound)
else:
    print(-1)