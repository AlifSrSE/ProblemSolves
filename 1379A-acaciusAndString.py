# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
def alif():
    n = int(input())
    s = input()
    t = "abacaba"
    found = False
    for i in range(n - 6):
        temp = list(s)
        ok = True
        for j in range(7):
            if temp[i + j] != '?' and temp[i + j] != t[j]:
                ok = False
                break
            temp[i + j] = t[j]
        if not ok:
            continue
        count = 0
        temp_str = "".join(temp)
        for j in range(n - 6):
            if temp_str[j:j+7] == t:
                count += 1
        if count == 1:
            for j in range(n):
                if temp[j] == '?':
                    temp[j] = 'z'
            found = True
            print("YES")
            print("".join(temp))
            break
    if not found:
        print("NO")

T = int(input())
for _ in range(T):
    alif()
