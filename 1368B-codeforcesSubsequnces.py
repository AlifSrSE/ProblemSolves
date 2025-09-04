# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    k = int(sys.stdin.readline())
    s = "codeforces"
    n = len(s)
    
    counts = [1] * n
    prod = 1
    i = 0
    
    while prod < k:
        prod //= counts[i]
        counts[i] += 1
        prod *= counts[i]
        i = (i + 1) % n
        
    result = []
    for j in range(n):
        result.append(s[j] * counts[j])
        
    sys.stdout.write("".join(result) + '\n')

def main():
    alif()

if __name__ == "__main__":
    main()
