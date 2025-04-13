# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(n, m, k):
    return min(k, n) * min(k, m)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    for _ in range(t):
        n = int(data[index])
        index += 1
        m = int(data[index])
        index += 1
        k = int(data[index])
        index += 1
        print(solve(n, m, k))

if __name__ == "__main__":
    main()