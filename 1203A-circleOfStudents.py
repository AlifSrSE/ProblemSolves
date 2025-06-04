# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1203/problem/A

def alif():
    q = int(input())
    for _ in range(q):
        n = int(input())
        p_list_str = input().split()
        p_list = [int(val) for val in p_list_str]
        prev = p_list[0]
        up = True
        down = True

        for i in range(1, n):
            x = p_list[i] 
            if up:
                if x == prev + 1:
                    pass
                elif x == 1 and prev == n:
                    pass
                else:
                    up = False

            if down:
                if x == prev - 1:
                    pass
                elif x == n and prev == 1:
                    pass
                else:
                    down = False 
            prev = x

        print("YES" if up or down else "NO")

if __name__ == "__main__":
    alif()