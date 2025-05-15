# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1177/problem/A

def alif(k):
    sequence = ""
    i = 1
    while len(sequence) < k:
        sequence += str(i)
        i += 1
    return int(sequence[k - 1])

if __name__ == "__main__":
    k = int(input())
    print(alif(k))
