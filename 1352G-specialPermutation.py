# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())

        if n < 4:
            print(-1)
        else:
            result = []
            for i in range(n, 0, -1):
                if i % 2 == 1:
                    result.append(str(i))
            
            result.append('4')
            result.append('2')

            for i in range(n, 0, -1):
                if i % 2 == 0 and i != 4 and i != 2:
                    result.append(str(i))
            
            print(' '.join(result))

if __name__ == "__main__":
    alif()