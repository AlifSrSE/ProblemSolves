# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        s = sys.stdin.readline().strip()

        z = 0
        for char in s:
            if char == '0':
                z += 1
            else:
                break
        
        a = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                a += 1
            else:
                break

        if z + a < n:
            z += 1
        
        sys.stdout.write('0' * z)
        sys.stdout.write('1' * a)
        sys.stdout.write('\n')

if __name__ == '__main__':
    main()
