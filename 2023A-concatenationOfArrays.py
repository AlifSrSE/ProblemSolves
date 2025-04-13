# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a1, a2):
    sorted_indices = sorted(range(len(a1)), key=lambda i: (min(a1[i], a2[i]), max(a1[i], a2[i])))
    result = []
    for i in sorted_indices:
        result.extend([a1[i], a2[i]])
    return ' '.join(map(str, result))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a1 = [0] * n
        a2 = [0] * n
        for i in range(n):
            a1[i], a2[i] = map(int, input().split())
        print(solve(a1, a2))