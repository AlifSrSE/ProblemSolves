# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    max_ans = 0
    
    for mx in range(1, 31):
        current_sum = 0
        
        for x in a:
            if x > mx:
                current_sum = 0
            else:
                current_sum += x
                if current_sum < 0:
                    current_sum = 0
            max_ans = max(max_ans, current_sum - mx)
    print(max_ans)

if __name__ == "__main__":
    alif()