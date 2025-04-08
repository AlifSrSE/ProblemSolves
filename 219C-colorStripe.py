# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

n, k = map(int, input().split())
stripe = input().strip()

if k == 2:
    totalA = 0
    totalB = 0
    for p in range(n):
        if stripe[p] == chr(ord('A') + (p % 2)):
            totalB += 1
        else:
            totalA += 1

    total = totalA
    offset = 0
    if totalB < totalA:
        total = totalB
        offset = 1

    print(total)
    print(''.join([chr(ord('A') + (p + offset) % 2) for p in range(n)]))
else:
    total = 0
    stripe = list(stripe)  

    if n >= 2 and stripe[1] == stripe[0]:
        total += 1
        for q in range(3):
            if (stripe[0] != chr(ord('A') + q)) and ((n == 2) or (n > 2 and stripe[2] != chr(ord('A') + q))):
                stripe[1] = chr(ord('A') + q)
                break

    for p in range(1, n - 1):
        if stripe[p] != stripe[p - 1]:
            continue
        total += 1
        if p >= 2 and stripe[p - 2] != stripe[p + 1]:
            stripe[p] = stripe[p - 2]
        else:
            for q in range(3):
                if (stripe[p - 1] != chr(ord('A') + q)) and (stripe[p + 1] != chr(ord('A') + q)):
                    stripe[p] = chr(ord('A') + q)
                    break

    if n > 1 and stripe[-1] == stripe[-2]:
        total += 1
        for q in range(3):
            if stripe[-2] != chr(ord('A') + q):
                stripe[-1] = chr(ord('A') + q)
                break

    print(total)
    print(''.join(stripe))