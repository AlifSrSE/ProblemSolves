# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = 5000
    n = int(data[0])
    counts = [0] * (N + 1)
    
    for num in map(int, data[1:n+1]):
        counts[num] += 1
    
    cumCounts = [0] * (N + 1)
    for k in range(1, N + 1):
        cumCounts[k] = cumCounts[k - 1] + counts[k]
    
    maxPresent = 0
    for k in range(1, N // 2 + 1):
        currentPresent = cumCounts[2 * k] - cumCounts[k - 1]
        if currentPresent > maxPresent:
            maxPresent = currentPresent
    
    print(n - maxPresent)

if __name__ == "__main__":
    main()