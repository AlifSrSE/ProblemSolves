# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    try:
        t_str = sys.stdin.readline()
        if not t_str:
            return
        t = int(t_str)
        
        while t > 0:
            for _ in range(9):
                line = sys.stdin.readline().strip()
                modified_line = line.replace('1', '2')
                sys.stdout.write(modified_line + '\n')
            
            t -= 1

    except (IOError, ValueError) as e:
        pass

if __name__ == "__main__":
    alif()