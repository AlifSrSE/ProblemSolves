# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1244/problem/C

def alif():
    n, m, w, d = map(int, input().split())
    x_found = -1

    for y in range(100000):
        current_m_remaining = m - y * d
        if current_m_remaining < 0:
            break
        if w != 0 and current_m_remaining % w == 0:
            x = current_m_remaining // w
            
            if x + y <= n:
                z = n - x - y
                print(f"{x} {y} {z}")
                x_found = x
                break       
    if x_found < 0:
        print("-1")

if __name__ == "__main__":
    alif()