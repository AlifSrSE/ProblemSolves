# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/2109/C2

ti = int(input())
for _ in range(ti):
    ni = int(input())
    
    print("mul 9", flush=True)
    response = input()
    if response == "-1":
        break
    
    print("digit", flush=True)
    response = input()
    if response == "-1":
        break
    
    print("digit", flush=True)
    response = input()
    if response == "-1":
        break
    
    print(f"add {ni - 9}", flush=True)
    response = input()
    if response == "-1":
        break
    
    print("!", flush=True)
    response = input()
    if response == "-1":
        break