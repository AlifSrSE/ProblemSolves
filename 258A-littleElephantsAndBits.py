# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

a = input().strip()
n = len(a)
result = []
found = False
for i in range(n):
    if a[i] == '0' and not found:
        found = True
        continue
    result.append(a[i])
if not found:
    result = result[:-1]
print(''.join(result))