
# Author: AlifSrSE
import sys

def solve(a, b, k):
    a_counts = [0] * 26
    b_counts = [0] * 26
    
    for char in a:
        a_counts[ord(char) - ord('a')] += 1
    for char in b:
        b_counts[ord(char) - ord('a')] += 1
        
    for i in range(25):
        if a_counts[i] < b_counts[i] or (a_counts[i] - b_counts[i]) % k != 0:
            return False
        
        surplus = a_counts[i] - b_counts[i]
        a_counts[i+1] += surplus
        
    return a_counts[25] == b_counts[25]

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t):
        n = int(input_data[ptr])
        k = int(input_data[ptr+1])
        a = input_data[ptr+2]
        b = input_data[ptr+3]
        ptr += 4
        results.append("Yes" if solve(a, b, k) else "No")
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()