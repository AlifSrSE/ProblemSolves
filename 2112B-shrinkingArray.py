# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/2112/problem/B

def alif():
    def is_beautiful(ai):
        for i in range(len(ai) - 1):
            if abs(ai[i] - ai[i + 1]) <= 1:
                return True
        return False
    ti = int(input())
    
    for _ in range(ti):
        ni = int(input())
        ai = list(map(int, input().split()))
        if is_beautiful(ai):
            print(0)
            continue
        
        for i in range(ni - 1):
            LI = min(ai[i], ai[i + 1])
            RI = max(ai[i], ai[i + 1])
            if i - 1 >= 0:
                v = ai[i - 1]
                if RI >= v - 1 and LI <= v + 1:
                    print(1)
                    break
            if i + 2 < ni:
                vi = ai[i + 2]
                if RI >= vi - 1 and LI <= vi + 1:
                    print(1)
                    break
        else:
            print(-1)

if __name__ == "__main__":
    alif()