# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a):
    values = list(map(int, a))
    
    result = sum(values)
    while len(values) != 1:
        values = [values[i + 1] - values[i] for i in range(len(values) - 1)]
        result = max(result, abs(sum(values)))
    
    return result

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a))

if __name__ == "__main__":
    main()
