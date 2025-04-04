# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve_test_case():
    n = int(input())
    
    p = [0] + list(map(int, input().split()))
    d = [0] + list(map(int, input().split()))
    
    comp = [0] * (n + 1)
    cycle_size = []
    cycle_id = 0
    
    for i in range(1, n + 1):
        if comp[i] != 0:
            continue
        cycle_id += 1
        cur = i
        count = 0
        while comp[cur] == 0:
            comp[cur] = cycle_id
            count += 1
            cur = p[cur]
        cycle_size.append(count) 
    
    forced = [False] * (cycle_id + 1)
    ans = 0
    
    result = []
    for i in range(1, n + 1):
        idx = d[i]
        cid = comp[idx]
        if not forced[cid]:
            forced[cid] = True
            ans += cycle_size[cid - 1]
        result.append(str(ans))
    
    print(" ".join(result))

def main():
    t = int(input())
    for _ in range(t):
        solve_test_case()

if __name__ == "__main__":
    main()
