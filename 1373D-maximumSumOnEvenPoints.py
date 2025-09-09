# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def max_subarray_sum(arr):
    max_so_far = 0
    current_max = 0
    for x in arr:
        current_max += x
        if current_max < 0:
            current_max = 0
        max_so_far = max(max_so_far, current_max)
    return max_so_far

def alif():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    initial_sum = sum(a[i] for i in range(0, n, 2))
    d1 = []

    for i in range(0, n - 1, 2):
        d1.append(a[i+1] - a[i])
    d2 = []
    
    for i in range(1, n - 1, 2):
        d2.append(a[i] - a[i+1])
        
    gain1 = max_subarray_sum(d1)
    gain2 = max_subarray_sum(d2)
    max_gain = max(gain1, gain2)
    print(initial_sum + max_gain)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()
