# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    
    n = int(data[idx]); idx += 1
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(data[idx]); idx += 1
    
    q = int(data[idx]); idx += 1
    queries = []
    for _ in range(q):
        l = int(data[idx]); r = int(data[idx+1]); x = int(data[idx+2])
        idx += 3
        queries.append((l, r, x))
    
    diff = [0] * (n + 1)
    for i in range(2, n + 1):
        diff[i] = a[i] - a[i-1]
    
    S = 0
    for i in range(2, n + 1):
        if diff[i] > 0:
            S += diff[i]
    
    base = a[1]
    
    def calculate_ans():
        return (base + S + 1) // 2
    
    res = []
    res.append(str(calculate_ans()))
    
    for l, r, x in queries:
        if l > 1:
            old_val = diff[l]
            diff[l] += x
            new_val = diff[l]
            if old_val > 0:
                S -= old_val
            if new_val > 0:
                S += new_val
        
        if r < n:
            old_val = diff[r + 1]
            diff[r + 1] -= x
            new_val = diff[r + 1]
            if old_val > 0:
                S -= old_val
            if new_val > 0:
                S += new_val
        
        if l == 1:
            base += x
        
        res.append(str(calculate_ans()))
    
    print("\n".join(res))

if __name__ == "__main__":
    main()