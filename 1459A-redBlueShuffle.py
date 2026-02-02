# Author: AlifSrSE
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1

    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1

        a = data[idx].lstrip('0') or '0'
        b = data[idx+1].lstrip('0') or '0'
        idx += 2

        if len(a) > len(b):
            out.append("RED")
        elif len(a) < len(b):
            out.append("BLUE")
        else:
            if a > b:
                out.append("RED")
            elif a < b:
                out.append("BLUE")
            else:
                out.append("EQUAL")

    print("\n".join(out))

if __name__ == "__main__":
    solve()
