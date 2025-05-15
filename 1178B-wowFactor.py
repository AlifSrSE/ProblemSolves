# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1178/problem/B

def alif(s):
    n = len(s)
    left_w_counts = [0] * n
    left_w_count = 0
    for i in range(n):
        if i > 0 and s[i] == 'v' and s[i - 1] == 'v':
            left_w_count += 1
        left_w_counts[i] = left_w_count

    right_w_counts = [0] * n
    right_w_count = 0
    for i in range(n - 1, -1, -1):
        if i < n - 1 and s[i] == 'v' and s[i + 1] == 'v':
            right_w_count += 1
        right_w_counts[i] = right_w_count

    return sum(left_w_counts[i] * right_w_counts[i] for i in range(n) if s[i] == 'o')

if __name__ == "__main__":
    s = input()
    print(alif(s))
