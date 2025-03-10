
import math
def main():
    #import sys
    #sys.stdin = open("input.txt", "r")
    #sys.stdout = open("output.txt", "w")
    #sys.stderr = open("error.txt", "w")
    
    n = int(input())
    ones = twos = threes = tx = 0
    arr = list(map(int, input().split()))
    
    for ai in arr:
        if ai == 4:
            tx += 1
        elif ai == 3:
            threes += 1
        elif ai == 2:
            twos += 1
        else:
            ones += 1
    
    if threes > ones:
        tx += threes
        tx += (twos // 2) + (twos % 2)
    elif threes < ones:
        tx += threes
        ones -= threes
        tx += (twos // 2)
        twos %= 2
        if twos:
            tx += 1
            ones -= 2
        if ones > 0:
            tx += ones // 4
            if ones % 4:
                tx += 1
    else: 
        tx += threes
        tx += (twos // 2) + (twos % 2)
    
    print(tx)

if __name__ == "__main__":
    main()