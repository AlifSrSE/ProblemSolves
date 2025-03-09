import sys

def solve():
    n = int(sys.stdin.readline().strip())
    fl = [0] * n
    fr = [0] * n
    a = []
    
    for i in range(n):
        l, r = map(int, sys.stdin.readline().split())
        a.append([l, r, i])
    
    a.sort(key=lambda x: (x[0], -x[1]))
    
    s = set()
    for i in range(n):
        l, r, idx = a[i]
        it = next((x for x in s if x >= r), None)
        fr[idx] = r if it is None else it
        if i < n - 1 and a[i + 1][0] == l and a[i + 1][1] == r:
            fr[idx] = r
        s.add(r)
    
    a.sort(key=lambda x: (-x[1], x[0]))
    s.clear()
    
    for i in range(n):
        l, r, idx = a[i]
        it = next((x for x in s if x <= -l), None)
        fl[idx] = l if it is None else -it
        if i < n - 1 and a[i + 1][0] == l and a[i + 1][1] == r:
            fl[idx] = l
        s.add(-l)
    
    a.sort(key=lambda x: x[2])
    
    for i in range(n):
        print(a[i][0] - a[i][1] + fr[i] - fl[i])


def main():
    tc = int(sys.stdin.readline().strip())
    for _ in range(tc):
        solve()

if __name__ == "__main__":
    main()