# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        a = int(data[idx])
        s = int(data[idx + 1])
        idx += 2
        
        v = []
        possible = True
        
        while possible and a > 0:
            x = a % 10
            a = a // 10
            y = s % 10
            s = s // 10
            
            if x <= y:
                v.append(y - x)
            elif s > 0:
                y += 10 * (s % 10)
                s = s // 10
                if y < x or y > 9 + x:
                    possible = False
                else:
                    v.append(y - x)
            else:
                possible = False
        
        if possible:
            v.append(s)
            b = 0
            for num in reversed(v):
                b = 10 * b + num
            print(b)
        else:
            print(-1)

if __name__ == "__main__":
    main()