# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

n = int(input())
rounds = [input().split() for _ in range(n)]

for i in range(n):
    rounds[i][1] = int(rounds[i][1])

scores = {}

for name, score in rounds:
    scores[name] = scores.get(name, 0) + score

max_score = max(scores.values())
candidates = {name for name, score in scores.items() if score == max_score}
running_scores = {}

for name, score in rounds:
    running_scores[name] = running_scores.get(name, 0) + score
    if running_scores[name] >= max_score and name in candidates:
        print(name)
        break