# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
n = int(input())
s = input()
t = input()
if s.count('1') != t.count('1') or s.count('0') != t.count('0'):
    print(-1)
    exit()
pos_s_1 = [i for i, ch in enumerate(s) if ch == '1']
pos_t_1 = [i for i, ch in enumerate(t) if ch == '1']
pos_s_0 = [i for i, ch in enumerate(s) if ch == '0']
pos_t_0 = [i for i, ch in enumerate(t) if ch == '0']
res = 0
for ps, pt in [(pos_s_1, pos_t_1), (pos_s_0, pos_t_0)]:
    max_diff = 0
    for i in range(len(ps)):
        diff = (pt[i] - ps[i]) % n
        if diff > max_diff:
            max_diff = diff
    if max_diff > res:
        res = max_diff
print(res)