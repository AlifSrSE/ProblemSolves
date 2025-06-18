# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1223/problem/B

def alif():
    q = int(input())
    
    for _ in range(q):
        s = input().strip()
        t = input().strip()
        s_set = set(s)
        has_common = any(ch in s_set for ch in t)
        print("YES" if has_common else "NO")

if __name__ == "__main__":
    alif()