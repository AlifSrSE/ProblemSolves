# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/contest/1151/problem/B

BIT_LIMIT = 10

def alif(a):
    n = len(a)
    m = len(a[0])

    for p in range(BIT_LIMIT):
        bits = [[(a[i][j] >> p) & 1 for j in range(m)] for i in range(n)]

        indices = find_indices(bits)
        if indices is not None:
            return "TAK\n" + ' '.join(str(i + 1) for i in indices)

    return "NIE"

def find_indices(bits):
    n = len(bits)
    m = len(bits[0])
    result = [0] * n

    for i in range(n):
        if len(set(bits[i])) == 2:
            bit = 1 ^ reduce_xor([bits[j][0] for j in range(n) if j != i])
            for j in range(m):
                if bits[i][j] == bit:
                    result[i] = j
                    break
            break

    for i in range(n):
        if result[i] == 0 and (i == 0 or result[i] != result[0]):
            result[i] = 0

    if reduce_xor([bits[i][result[i]] for i in range(n)]) == 1:
        return result
    else:
        return None

def reduce_xor(lst):
    result = 0
    for x in lst:
        result ^= x
    return result

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    print(alif(a))
