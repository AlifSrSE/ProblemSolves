# Author: AlifSrSe
# date: 2025-03-25
# https://codeforces.com/problemset/problem/2090/D
 
import sys

LIMIT = 200_000
is_prime = [True] * (LIMIT + 1)

def sieve_of_eratosthenes():
    global is_prime
    if LIMIT >= 1:
        is_prime[1] = False

    for i in range(2, int(LIMIT**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, LIMIT + 1, i):
                is_prime[j] = False

def get_permutation(num):
    prime_pos = 1
    for i in range(1, (2 * num) // 3 + 1):
        if is_prime[i]:
            prime_pos = i

    sequence = [prime_pos]
    left = prime_pos - 1
    right = prime_pos + 1

    while True:
        if right > num:
            break
        sequence.append(right)
        right += 1

        if left < 1:
            break
        sequence.append(left)
        left -= 1

    for i in range(1, left + 1):
        sequence.append(i)
    for i in range(right, num + 1):
        sequence.append(i)

    print(" ".join(map(str, sequence)))

def main():
    sieve_of_eratosthenes()
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        num = int(sys.stdin.readline().strip())
        get_permutation(num)

if __name__ == "__main__":
    main()
