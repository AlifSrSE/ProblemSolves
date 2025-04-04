# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(s, t):
    same_suffix_length = 0
    while same_suffix_length + 1 <= min(len(s), len(t)) and s[len(s) - 1 - same_suffix_length] == t[len(t) - 1 - same_suffix_length]:
        same_suffix_length += 1
    return len(s) + len(t) - 2 * same_suffix_length

def main():
    s = input()
    t = input()
    print(solve(s, t))

if __name__ == "__main__":
    main()