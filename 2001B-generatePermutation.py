# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(n):
    if n % 2 == 0:
        return "-1"
    
    result = []
    for i in range(n // 2 + 1):
        result.append(n // 2 + 1 - i)
    for i in range(n // 2 + 1, n):
        result.append(i + 1)
    
    return ' '.join(map(str, result))

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
        print(solve(n))

if __name__ == "__main__":
    main()