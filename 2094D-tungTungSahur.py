# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def check_pattern(p, s):
    i = j = 0
    while i < len(p):
        current_char = p[i]
        count_p = 0
        while i < len(p) and p[i] == current_char:
            count_p += 1
            i += 1
        if j >= len(s) or s[j] != current_char:
            return False
        count_s = 0
        while j < len(s) and s[j] == current_char:
            count_s += 1
            j += 1
        if not (count_p <= count_s <= 2 * count_p):
            return False
    return j == len(s)

def main():
    t = int(input())
    for _ in range(t):
        p = input().strip()
        s = input().strip()
        print("YES" if check_pattern(p, s) else "NO")

if __name__ == "__main__":
    main()
