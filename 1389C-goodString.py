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
        s = data[pointer]
        pointer += 1
        n = len(s)
        mx = 0
        
        for a in range(10):
            a_char = str(a)
            for b in range(10):
                b_char = str(b)
                state = 0
                cnt = 0
                for char in s:
                    if state == 1 and char == a_char:
                        cnt += 1
                        state = 1 - state
                    elif state == 0 and char == b_char:
                        cnt += 1
                        state = 1 - state
                if a != b and cnt % 2 != 0:
                    cnt -= 1
                mx = max(mx, cnt)
        output.append(str(n - mx))
    sys.stdout.write('\n'.join(output) + '\n')

alif()