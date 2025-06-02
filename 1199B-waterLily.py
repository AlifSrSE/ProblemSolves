# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1199/problem/B

def alif():
    h, l = map(float, input().split())    
    ans = (l * l - h * h) / (2.0 * h) 
    print(f"{ans:.8f}")

if __name__ == "__main__":
    alif()