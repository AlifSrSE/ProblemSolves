#Author: AlifSrSE

import sys

def solve(tiles, m):
    if m % 2 != 0:
        return False
    for tile in tiles:
        if tile[0][1] == tile[1][0]:
            return True
    return False

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t):
        n = int(input_data[ptr])
        m = int(input_data[ptr+1])
        ptr += 2
        tiles = []
        for _ in range(n):
            r1c1 = int(input_data[ptr])
            r1c2 = int(input_data[ptr+1])
            r2c1 = int(input_data[ptr+2])
            r2c2 = int(input_data[ptr+3])
            tiles.append([[r1c1, r1c2], [r2c1, r2c2]])
            ptr += 4
        results.append("YES" if solve(tiles, m) else "NO")
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()