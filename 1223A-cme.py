# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1223/problem/A

def alif():
    q = int(input())
    
    for _ in range(q):
        n = int(input())
        
        if n == 2:
            result = 2
        elif n % 2 == 0:
            result = 0
        else:
            result = 1
        print(result)

if __name__ == "__main__":
    alif()