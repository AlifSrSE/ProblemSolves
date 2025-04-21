# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/contest/236/problem/D

def calculate_expected_score(n, probabilities):
    total_score = 0.0
    sum1 = 0.0
    sum2 = 0.0
    sum3 = 0.0
    
    p = [0.0] + probabilities + [0.0]

    for i in range(1, n + 1):
        sum3 *= p[i]
        sum3 += p[i] * (1 - p[i - 1])
        sum2 *= p[i]
        sum1 *= p[i]

        contribution = (sum3 * i * i - i * sum2 + sum1) * (1 - p[i + 1])
        total_score += contribution

        sum2 += 2 * i * (1 - p[i])
        sum1 += i * i * (1 - p[i])

    return total_score

n = int(input())
probabilities = list(map(float, input().split()))
result = calculate_expected_score(n, probabilities)

print("%.12f" % result)