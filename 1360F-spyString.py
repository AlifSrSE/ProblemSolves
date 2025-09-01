# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def check(s1, s2):
    diff_count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff_count += 1
    return diff_count <= 1

def alif():
    n, m = map(int, sys.stdin.readline().split())
    a = [sys.stdin.readline().strip() for _ in range(n)]

    is_first_string_valid = True
    for i in range(1, n):
        if not check(a[0], a[i]):
            is_first_string_valid = False
            break
    
    if is_first_string_valid:
        print(a[0])
        return

    for p in range(m):
        for c_ord in range(ord('a'), ord('z') + 1):
            c = chr(c_ord)
            test_string_list = list(a[0])
            test_string_list[p] = c
            test_string = "".join(test_string_list)
            is_valid = True

            for i in range(1, n):
                if not check(test_string, a[i]):
                    is_valid = False
                    break
            
            if is_valid:
                print(test_string)
                return

    print("-1")

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()