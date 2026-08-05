# Author: AlifSrSE
import sys

def solve(poem):
    letters = list(poem)
    result = 0
    n = len(letters)
    for i in range(1, n):
        # Check condition for length 2 or length 3 palindrome
        if letters[i] == letters[i - 1] or (i >= 2 and letters[i] == letters[i - 2]):
            result += 1
            # Mark as a placeholder character that won't match anything
            letters[i] = '#' 
    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = [str(solve(poem)) for poem in input_data[1 : t + 1]]
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()