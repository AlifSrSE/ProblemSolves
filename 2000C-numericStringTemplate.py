# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def compress(values):
    value_to_compressed = {}
    compressed = []
    for value in values:
        if value not in value_to_compressed:
            value_to_compressed[value] = len(value_to_compressed)
        compressed.append(value_to_compressed[value])
    return compressed

def solve(a, s_list):
    compressed_a = compress(a)
    result = []

    for si in s_list:
        s_compressed = compress(list(map(ord, si)))
        result.append("YES" if s_compressed == compressed_a else "NO")

    return "\n".join(result)

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    s_list = [input().strip() for _ in range(m)]
    print(solve(a, s_list))
