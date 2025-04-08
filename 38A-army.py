# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

n = int(input())

years = [0] * (n + 1)
years[0] = years[1] = 0

numbers = list(map(int, input().split()))
for k in range(2, n + 1):
    years[k] = years[k - 1] + numbers[k-2]

currentRank, futureRank = map(int, input().split())

print(years[futureRank] - years[currentRank])