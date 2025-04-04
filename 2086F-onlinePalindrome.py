# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def opt(x, y):
    if x == y:
        print("0 0")
    else:
        print(x + 1, y + 1)

def gen(c0, c1, tag):
    cc0 = c0 // 2
    cc1 = c1 // 2
    for i in range(cc0 + cc1):
        p = i * 2
        if p >= cc0 + cc1:
            p = cc0 * 2 + cc1 * 2 - 1 - p
        if i < cc0:
            b[p][tag] = 0
        else:
            b[p][tag] = 1
    if c0 % 2 == 1:
        b[(c0 + c1) // 2][tag] = 0
    else:
        b[(c0 + c1) // 2][tag] = 1
    for i in range((c0 + c1) // 2):
        b[c0 + c1 - 1 - i][tag] = b[i][tag]

def check(n, tag):
    c = 0
    a[n] = tag
    for i in range(n + 1):
        if a[i] != b[i][tag]:
            c += 1
    return c <= 2

def main():
    n = 1
    c0 = 0
    c1 = 0
    a = [0] * 100
    b = [[0, 0] for _ in range(100)]
    
    s = input().strip()
    a[0] = ord(s[0]) - ord('a')
    opt(0, 0)
    if a[0] == 0:
        c0 += 1
    else:
        c1 += 1
    
    while True:
        s = input().strip()
        if s[0] == '0':
            return
        
        a[n] = ord(s[0]) - ord('a')
        if a[n] == 0:
            c0 += 1
        else:
            c1 += 1
        n += 1
        
        gen(c0 + 1, c1, 0)
        gen(c0, c1 + 1, 1)
        
        flag = 0
        for i in range(n):
            for j in range(i, n):
                a[i], a[j] = a[j], a[i]
                if check(n, 0) and check(n, 1):
                    opt(i, j)
                    flag = 1
                    break
                a[i], a[j] = a[j], a[i]
            if flag:
                break
        
        assert flag
        
        s = input().strip()
        a[n] = ord(s[0]) - ord('a')
        if a[n] == 0:
            c0 += 1
        else:
            c1 += 1
        flag = a[n]
        n += 1
        
        p1 = -1
        p2 = -1
        for i in range(n):
            if a[i] != b[i][flag]:
                if p1 == -1:
                    p1 = i
                else:
                    p2 = i
        
        if p1 == -1 or p2 == -1:
            opt(0, 0)
        else:
            a[p1], a[p2] = a[p2], a[p1]
            opt(p1, p2)

if __name__ == "__main__":
    main()
