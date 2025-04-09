# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def can_partition(x: int, a: list[int], k: int) -> bool:
    if x == 0:
        return True
    count_segments = 0
    seen = [False] * x
    needed = x
    for num in a:
        if num < x and not seen[num]:
            seen[num] = True
            needed -= 1
        if needed == 0:
            count_segments += 1
            if count_segments >= k:
                return True
            seen = [False] * x
            needed = x
    return False
 
def mexx(a: list[int], k: int) -> int:
    freq = {}
    for num in a:
        freq[num] = freq.get(num, 0) + 1
    x0 = 0
    while True:
        if freq.get(x0, 0) < k:
            break
        x0 += 1
 
    lo = 0
    hi = x0 + 1
    while lo < hi:
        mid = (lo + hi) // 2
        if can_partition(mid, a, k):
            lo = mid + 1
        else:
            hi = mid
    return lo - 1
 
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(mexx(a, k))