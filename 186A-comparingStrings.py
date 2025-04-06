# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def same_race(genome1, genome2):
    if len(genome1) != len(genome2):
        return False
    
    diff_positions = []
    for i in range(len(genome1)):
        if genome1[i] != genome2[i]:
            diff_positions.append(i)
            if len(diff_positions) > 2:
                return False
    
    if len(diff_positions) == 2:
        i, j = diff_positions
        return genome1[i] == genome2[j] and genome1[j] == genome2[i]
    elif len(diff_positions) == 0:
        from collections import defaultdict
        freq = defaultdict(int)
        for c in genome1:
            freq[c] += 1
            if freq[c] >= 2:
                return True
        return False
    else:
        return False

genome1 = input().strip()
genome2 = input().strip()

if same_race(genome1, genome2):
    print("YES")
else:
    print("NO")