# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

k = int(input())
input_str = input().strip()
alpha_size = 26
letters = [0] * alpha_size
output = ""

for char in input_str:
    letters[ord(char) - ord('a')] += 1

for u in range(alpha_size):
    if letters[u] == 0:
        continue
    elif letters[u] % k == 0:
        output += chr(ord('a') + u) * (letters[u] // k)
    else:
        output = "-1"
        break

if output == "-1":
    print(output)
else:
    print(output * k)