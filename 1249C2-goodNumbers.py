# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1249/problem/C2

import sys

def alif():
    q = int(sys.stdin.readline())

    for _ in range(q):
        n = int(sys.stdin.readline())
        b = []

        if n == 0:
            b.append(0)
        else:
            temp_n = n
            while temp_n > 0:
                b.append(temp_n % 3)
                temp_n //= 3
        carry = 0
        
        for p in range(len(b)):
            b[p] += carry
            carry = 0

            if b[p] > 1:
                for u in range(p + 1):
                    b[u] = 0
                carry = 1
                
        if carry:
            b.append(1)
        m = 0
        current_power_of_3 = 1

        for p in range(len(b)):
            m += b[p] * current_power_of_3
            current_power_of_3 *= 3
        
        sys.stdout.write(f"{m}\n")

if __name__ == "__main__":
    alif()