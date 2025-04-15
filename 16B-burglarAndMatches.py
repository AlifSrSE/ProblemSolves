# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/16/B

def solve():
    n, m = map(int, input().split())
    cont_vec = []
    for _ in range(m):
        boxes, matches = map(int, input().split())
        cont_vec.append({'boxes': boxes, 'matches': matches})

    cont_vec.sort(key=lambda x: x['matches'])

    capacity = n
    output = 0
    for k in range(m - 1, -1, -1):
        if capacity > cont_vec[k]['boxes']:
            output += cont_vec[k]['boxes'] * cont_vec[k]['matches']
            capacity -= cont_vec[k]['boxes']
        else:
            output += capacity * cont_vec[k]['matches']
            break

    print(output)

solve()