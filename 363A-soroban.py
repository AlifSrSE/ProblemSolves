# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def digitize(n):
    return [int(d) for d in reversed(str(n))]

def print_digit(digit):
    if digit < 5:
        print("O-|", end="")
    else:
        print("-O|", end="")
        digit -= 5

    print("O" * digit + "-" + "O" * (4 - digit))

def main():
    n = int(input())
    digits = digitize(n)
    for d in digits:
        print_digit(d)

if __name__ == "__main__":
    main()
