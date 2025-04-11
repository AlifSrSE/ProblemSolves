# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(s):
    return s.count('1')

def main():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        print(solve(s))

if __name__ == "__main__":
    main()
