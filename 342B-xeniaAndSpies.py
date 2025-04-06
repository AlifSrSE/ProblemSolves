# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

n, m, s, f = map(int, input().split())
watched = []
for _ in range(m):
    ti, li, ri = map(int, input().split())
    watched.append((ti, li, ri))

res = []
current_step = 1
current_pos = s
direction = 1 if f > s else -1
watched_ptr = 0

while current_pos != f:
    if watched_ptr < m and current_step == watched[watched_ptr][0]:
        t, l, r = watched[watched_ptr]
        next_pos = current_pos + direction
        if (l <= current_pos <= r) or (l <= next_pos <= r):
            res.append('X')
        else:
            res.append('R' if direction == 1 else 'L')
            current_pos += direction
        watched_ptr += 1
    else:
        res.append('R' if direction == 1 else 'L')
        current_pos += direction
    current_step += 1

print(''.join(res))