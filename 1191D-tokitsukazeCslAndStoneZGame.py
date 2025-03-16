
# Author : AlifSrSE
# Date : 2025-03-15
# Problem link : https://codeforces.com/contest/1191/problem/D
 
n = int(input())
a = list(map(int, input().split()))
 
xsum = 0
sum_ = 0
 
for num in a:
    xsum ^= num
    sum_ += num
 
if sum_ == 0:
    print("cslnb")
elif xsum == 0:
    print("sjfnb")
else:
    if n % 2 == 0:
        print("cslnb")
    else:
        print("sjfnb")