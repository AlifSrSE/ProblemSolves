# Author : AlifSrSE
# Date : 2025-03-17
# Problem link : https://codeforces.com/contest/1985/problem/F

def main():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))
    
    index = 0
    t = data[index]  
    index += 1
    
    for _ in range(t):
        h = data[index] 
        n = data[index + 1] 
        index += 2
        
        a = data[index:index + n]  
        index += n
        
        c = data[index:index + n] 
        index += n
        
        print(solve(h, a, c))

def solve(h, a, c):
    result = -1
    lower = 1
    upper = min(
        [1 + (max(0, h - a[i]) + a[i] - 1) // a[i] * c[i] for i in range(len(a))]
    )
    
    while lower <= upper:
        middle = (lower + upper) // 2
        if check(h, a, c, middle):
            result = middle
            upper = middle - 1
        else:
            lower = middle + 1
    
    return result

def check(h, a, c, turn):
    total_damage = sum(a[i] + (turn - 1) // c[i] * a[i] for i in range(len(a)))
    return total_damage >= h

if __name__ == "__main__":
    main()