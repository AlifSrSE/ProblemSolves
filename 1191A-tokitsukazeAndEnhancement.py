# Author : AlifSrSE
# Date : 2025-03-14
# Problem link : https://codeforces.com/contest/1191/problem/A
 
x = int(input())
 
if x % 4 == 0:
    print("1 A")
elif x % 4 == 1:
    print("0 A")
elif x % 4 == 2:
    print("1 B")
else:
    print("2 A")