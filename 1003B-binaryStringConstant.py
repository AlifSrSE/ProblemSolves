# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a, b, x):
    result = ""
    zero_or_one = a >= b
    for i in range(x + 1, 0, -1):
        if zero_or_one:
            if i <= 2:
                while a != 0:
                    result += "0"
                    a -= 1
            else:
                result += "0"
                a -= 1
        else:
            if i <= 2:
                while b != 0:
                    result += "1"
                    b -= 1
            else:
                result += "1"
                b -= 1
        zero_or_one = not zero_or_one
    return result

def main():
    a, b, x = map(int, input().split())
    print(solve(a, b, x))

if __name__ == "__main__":
    main()