# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

x, y, a, b = map(int, input().split())
results = []

for ci in range(a, x + 1):
    for di in range(b, y + 1):
        if ci > di:
            results.append((ci, di))

results.sort()
print(len(results))
for pair in results:
    print(pair[0], pair[1])