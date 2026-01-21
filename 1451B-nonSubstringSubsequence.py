# Author: AlifSrSE
import sys

def solve(s, l, r):
    first_char = s[l-1]
    last_char = s[r-1]
    prefix_match = first_char in s[:l-1]
    suffix_match = last_char in s[r:]
    
    return prefix_match or suffix_match

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    ptr = 1
    output = []
    
    for _ in range(t):
        n = int(input_data[ptr])
        q = int(input_data[ptr+1])
        s = input_data[ptr+2]
        ptr += 3
        for _ in range(q):
            l = int(input_data[ptr])
            r = int(input_data[ptr+1])
            ptr += 2
            output.append("YES" if solve(s, l, r) else "NO")
            
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    main()