# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
def alif():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        result = 0

        for j in range(n):
            freq_after = [0] * (n + 1)
            for l in range(j + 2, n):
                freq_after[a[l]] += 1
                
            freq_before = [0] * (n + 1)
            for i in range(j):
                freq_before[a[i]] += 1
                
            for k in range(j + 1, n):
                result += freq_before[a[k]] * freq_after[a[j]]
                freq_after[a[k]] -= 1
            
        print(result)

alif()