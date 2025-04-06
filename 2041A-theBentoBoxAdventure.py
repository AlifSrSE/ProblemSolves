# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def main():
    total = 15
    numbers = list(map(int, input().split()))
    for i in range(4):
        total -= numbers[i]
    print(total)

if __name__ == "__main__":
    main()
