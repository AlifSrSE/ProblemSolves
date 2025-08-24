# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    try:
        t = int(sys.stdin.readline())
    except (IOError, ValueError):
        return

    for _ in range(t):
        try:
            n = int(sys.stdin.readline())
            a = list(map(int, sys.stdin.readline().split()))
        except (IOError, ValueError):
            continue

        a.sort()
        left = (n - 1) // 2
        right = (n + 1) // 2
        result = []
        
        while left >= 0 or right < n:
            if left >= 0:
                result.append(a[left])
                left -= 1
            
            if right < n:
                result.append(a[right])
                right += 1
        
        print(*result)

if __name__ == "__main__":
    alif()