# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1198/problem/A

def alif():
    n, b_val = map(int, input().split())
    bits = (8 * b_val) // n  # Maximum bits per value
    range_val = 1 << bits  # Maximum number of distinct values (2^bits)
    a = list(map(int, input().split()))
    a.sort()  # Sort the array for efficient range processing
    
    chg = n  # Initialize to maximum possible changes
    # Try each starting index for the range
    for i in range(n):
        # Count elements outside the range [a[i], a[i] + range_val - 1]
        count = 0
        for j in range(n):
            if a[j] < a[i] or a[j] > a[i] + range_val - 1:
                count += 1
        chg = min(chg, count)
    
    print(chg)

if __name__ == "__main__":
    alif()