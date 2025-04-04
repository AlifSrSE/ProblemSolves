# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n, k = map(int, input().split())
    ids = list(map(int, input().split()))

    screen = []
    seen = set()

    for id_val in ids:
        if id_val in seen:
            continue
        else:
            if len(screen) == k:
                removed_id = screen.pop()
                seen.remove(removed_id)
            screen.insert(0, id_val)
            seen.add(id_val)

    print(len(screen))
    print(*screen)

solve()