# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

MOD = 1000000007

def modMul(a, b):
    return (a % MOD) * (b % MOD) % MOD

def precomputeFactorials(n):
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = modMul(fact[i - 1], i)
    return fact

def computeMex(S):
    cur = 0
    while cur in S:
        cur += 1
    return cur

def main():
    T = int(input())  
    for _ in range(T):
        n = int(input()) 
        A = list(map(int, input().split())) 
        
        used = [False] * n
        valid = True
        
        for i in range(n):
            if A[i] != -1:
                if used[A[i]]:
                    valid = False
                    break
                used[A[i]] = True
        
        if not valid:
            print(0)
            continue
        
        missingVals = [v for v in range(n) if not used[v]]
        m = len(missingVals)
        
        fact = precomputeFactorials(m)
        
        prefixMissing = [0] * n
        for i in range(n):
            prefixMissing[i] = 1 if A[i] == -1 else 0
            if i > 0:
                prefixMissing[i] += prefixMissing[i - 1]
        
        ans = 0
        
        for l in range(n):
            for r in range(l, n):
                t = prefixMissing[r] - (prefixMissing[l - 1] if l > 0 else 0)
                
                segFixed = set()
                for i in range(l, r + 1):
                    if A[i] != -1:
                        segFixed.add(A[i])
                
                segSum = 0
                idx = list(range(m))
                
                def gen(start, left, comb):
                    nonlocal segSum
                    if left == 0:
                        U = segFixed.copy()
                        for x in comb:
                            U.add(missingVals[x])
                        curMex = computeMex(U)
                        segSum = (segSum + curMex) % MOD
                        return
                    
                    for i in range(start, m - left + 1):
                        comb.append(i)
                        gen(i + 1, left - 1, comb)
                        comb.pop()
                
                if t <= m:
                    gen(0, t, [])
                
                weight = modMul(fact[t], fact[m - t])
                segContribution = modMul(segSum, weight)
                ans = (ans + segContribution) % MOD
        
        print(ans)

if __name__ == "__main__":
    main()
