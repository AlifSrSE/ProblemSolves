# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    s = input()
    mod = 10**9 + 7

    distinct_sequences = set()
    q = [(list(map(int, list(s))), 0)]
    distinct_sequences.add(tuple(map(int, list(s))))

    while q:
        current_s, operations = q.pop(0)
        m = len(current_s)

        if operations < n - 2:
            for i in range(m - 2):
                subarray = sorted(current_s[i:i+3])
                median = subarray[1]
                j = -1
                for k in range(i, m):
                    if current_s[k] == median:
                        j = k
                        break

                if j != -1:
                    next_s = current_s[:j] + current_s[j+1:]
                    next_s_tuple = tuple(next_s)
                    if next_s_tuple not in distinct_sequences:
                        distinct_sequences.add(next_s_tuple)
                        q.append((next_s, operations + 1))

    print(len(distinct_sequences) % mod)

t = int(input())
for _ in range(t):
    solve()