# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def main():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        grid = [list(map(int, input().split())) for _ in range(n)]
        
        perm = [0] * (2 * n + 1) 
        
        for i in range(n):
            for j in range(n):
                index = i + j + 2
                if perm[index] == 0:
                    perm[index] = grid[i][j]
        
        seen = [False] * (2 * n + 1)
        for k in range(2, 2 * n + 1):
            seen[perm[k]] = True
        
        for num in range(1, 2 * n + 1):
            if not seen[num]:
                perm[1] = num
                break
        
        print(*perm[1:2 * n + 1])

if __name__ == "__main__":
    main()
