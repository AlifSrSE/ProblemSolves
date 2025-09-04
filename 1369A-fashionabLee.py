# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        if n % 4 == 0:
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")

if __name__ == "__main__":
    main()
