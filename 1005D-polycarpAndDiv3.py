# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(s):
    result = 0
    seen = {0}
    sum_val = 0
    for c in s:
        sum_val = (sum_val + int(c)) % 3
        if sum_val in seen:
            result += 1
            seen = {0}
            sum_val = 0
        else:
            seen.add(sum_val)
    return result

def main():
    s = input()
    print(solve(s))

if __name__ == "__main__":
    main()