# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def main():
    t = int(input())
    for _ in range(t):
        w, b = map(int, input().split())
        lo, hi = 0, 64000
        while lo < hi:
            mid = (lo + hi + 1) // 2
            rw, rb = w, b
            for i in range(mid, 0, -1):
                if rw > rb:
                    rw -= i
                else:
                    rb -= i
            if min(rw, rb) >= 0:
                lo = mid
            else:
                hi = mid - 1
        print(lo)

if __name__ == "__main__":
    main()
