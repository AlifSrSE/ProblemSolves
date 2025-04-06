# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

n = int(input())
goals = [input().strip() for _ in range(n)]

from collections import defaultdict

goal_counts = defaultdict(int)
for team in goals:
    goal_counts[team] += 1

teams = list(goal_counts.keys())
if len(teams) == 1:
    print(teams[0])
else:
    if goal_counts[teams[0]] > goal_counts[teams[1]]:
        print(teams[0])
    else:
        print(teams[1])