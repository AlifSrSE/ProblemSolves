# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    data = sys.stdin.read().split()

    if not data:
        return
    t = int(data[0])
    pointer = 1
    output = []

    for _ in range(t):
        n = int(data[pointer])
        pointer += 1

        if n <= 30:
            output.append("NO")
        elif n == 36 or n == 40 or n == 44:
            output.append(f"YES\n6 10 15 {n - 31}")
        else:
            output.append(f"YES\n6 10 14 {n - 30}")

    sys.stdout.write('\n'.join(output) + '\n')

alif()
