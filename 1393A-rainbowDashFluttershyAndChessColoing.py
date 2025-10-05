import sys

def alif():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    t = data[0]
    p = 1
    output = []

    for _ in range(t):
        x = data[p]
        p += 1
        result = 1 + x // 2
        output.append(str(result))
    sys.stdout.write('\n'.join(output) + '\n')

alif()