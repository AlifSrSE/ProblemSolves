# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t_str = sys.stdin.readline()
    if not t_str:
        return
    t = int(t_str)

    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        power_of_10 = 1
        round_numbers = []

        while n > 0:
            if n % 10 != 0:
                round_numbers.append((n % 10) * power_of_10)
            n //= 10
            power_of_10 *= 10
        
        print(len(round_numbers))
        print(*round_numbers)

if __name__ == "__main__":
    alif()