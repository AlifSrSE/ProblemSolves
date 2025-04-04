# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(s):
    count1 = s.count('1')
    remaining = "".join(ch for ch in s if ch != '1')

    index = 0
    while index < len(remaining) and remaining[index] == '0':
        index += 1

    return f"{remaining[:index]}{'1' * count1}{remaining[index:]}"

def main():
    s = input()
    print(solve(s))

if __name__ == "__main__":
    main()