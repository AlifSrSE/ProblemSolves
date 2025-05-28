# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1194/problem/B

def alif():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        nr, nc = map(int, input().split())
        v = []
        for p in range(nr):
            v.append(input())
        
        rowcount = [0] * nr
        colcount = [0] * nc
        
        for row in range(nr):
            for col in range(nc):
                if v[row][col] == '.':
                    continue
                rowcount[row] += 1
                colcount[col] += 1
        res = nr + nc 
        
        for row in range(nr):
            for col in range(nc):
                tmp = (nr - rowcount[row]) + (nc - colcount[col])
                if v[row][col] == '.':
                    tmp -= 1
                res = min(res, tmp)
        
        print(res)

if __name__ == "__main__":
    alif()