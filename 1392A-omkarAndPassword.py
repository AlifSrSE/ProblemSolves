# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    data = list(map(int, sys.stdin.read().split()))

    if not data:
        return
    t = data[0]
    pointer = 1
    output = []

    for _ in range(t):
        n = data[pointer]
        pointer += 1
        a = data[pointer : pointer + n]
        is_same = len(set(a)) == 1
        result = n if is_same else 1
        output.append(str(result))
        pointer += n

    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == "__main__":
    alif()