# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    n = int(sys.stdin.readline())
    sys.stdout.write(str(4 + 3 * n) + '\n')
    sys.stdout.write("0 0\n")
    sys.stdout.write("0 1\n")
    sys.stdout.write("1 0\n")
    sys.stdout.write("1 1\n")
    
    for p in range(n):
        sys.stdout.write(f"{p + 1} {p + 2}\n")
        sys.stdout.write(f"{p + 2} {p + 1}\n")
        sys.stdout.write(f"{p + 2} {p + 2}\n")

def main():
    alif()

if __name__ == '__main__':
    main()
