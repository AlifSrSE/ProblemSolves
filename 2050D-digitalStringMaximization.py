# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(s):
    digits = [int(c) for c in s]

    changed = True
    while changed:
        changed = False
        for i in range(len(digits) - 1):
            if digits[i + 1] >= digits[i] + 2:
                digits[i], digits[i + 1] = digits[i + 1] - 1, digits[i]
                changed = True

    return ''.join(map(str, digits))

def main():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        print(solve(s))

if __name__ == "__main__":
    main()
