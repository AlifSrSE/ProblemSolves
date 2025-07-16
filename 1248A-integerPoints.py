# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1248/problem/A

def alif():
    t = int(input())

    for _ in range(t):
        n = int(input())
        a_elements = list(map(int, input().split()))
        a_counts = [0, 0] 
        
        for x in a_elements:
            a_counts[x % 2] += 1
        
        m = int(input())
        b_elements = list(map(int, input().split()))
        b_counts = [0, 0]

        for x in b_elements:
            b_counts[x % 2] += 1
        
        ans = a_counts[0] * b_counts[0] + a_counts[1] * b_counts[1]
        print(ans)

if __name__ == "__main__":
    alif()