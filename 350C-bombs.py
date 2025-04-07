# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def main():
    n = int(input())
    point_vec = []

    total = 0
    for _ in range(n):
        a, b = map(int, input().split())
        dist = abs(a) + abs(b)
        point_vec.append({'x': a, 'y': b, 'dist': dist})
        total += 2 * (a != 0) + 2 * (b != 0) + 2

    print(total)

    point_vec.sort(key=lambda p: p['dist'])

    for p in point_vec:
        x, y = p['x'], p['y']
        hf, hb = ('R', 'L') if x > 0 else ('L', 'R')
        vf, vb = ('U', 'D') if y > 0 else ('D', 'U')
        ht, vt = abs(x), abs(y)

        if ht > 0:
            print(f"1 {ht} {hf}")
        if vt > 0:
            print(f"1 {vt} {vf}")
        print("2")
        if ht > 0:
            print(f"1 {ht} {hb}")
        if vt > 0:
            print(f"1 {vt} {vb}")
        print("3")

if __name__ == "__main__":
    main()
