# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    h, w = map(int, input().split())
    
    height = [0] * (h + 1)
    width = [0] * (w + 1)
    
    height[1:] = list(map(int, input().split()))
    width[1:] = list(map(int, input().split()))
    
    ans = 1
    md = 1000000007
    
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if (i - 1) == width[j] and (j - 1) < height[i]:
                ans = 0
                break
            if (i - 1) < width[j] and (j - 1) == height[i]:
                ans = 0
                break
            if (i - 1) > width[j] and (j - 1) > height[i]:
                ans = (ans * 2) % md
        if ans == 0:
            break
    
    print(ans)

solve()