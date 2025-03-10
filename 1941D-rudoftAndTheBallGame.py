# Author : AlifSrSE
# Date : 2025-03-09
# Problem link : https://codeforces.com/contest/1941/problem/D

def solve(n, r, c, x):
    players = {x - 1}
    
    for i in range(len(r)):
        new_players = set()
        for player in players:
            if c[i] in ('0', '?'):
                new_players.add((player + r[i]) % n)
            if c[i] in ('1', '?'):
                new_players.add((player - r[i]) % n)
        players = new_players

    return f"{len(players)}\n{' '.join(str(p + 1) for p in sorted(players))}"


def main():
    t = int(input().strip())
    for _ in range(t):
        n, m, x = map(int, input().split())
        r = []
        c = []
        for _ in range(m):
            ri, ci = input().split()
            r.append(int(ri))
            c.append(ci)

        print(solve(n, r, c, x))


if __name__ == "__main__":
    main()
