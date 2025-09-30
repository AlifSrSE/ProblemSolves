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
        a = [int(x) for x in data[pointer : pointer + n]]
        pointer += n
        rem = 0
        state = False

        for p in range(n - 2, -1, -1):
            if not state and a[p] >= a[p + 1]:
                continue
            elif not state and a[p] <= a[p + 1]:
                state = True
            elif state and a[p] <= a[p + 1]:
                continue
            elif state and a[p] > a[p + 1]:
                rem = p + 1
                break

        output.append(f"{rem}")
    sys.stdout.write('\n'.join(output) + '\n')

alif()
