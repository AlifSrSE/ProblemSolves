# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(y):
    if bin(y).count('1') == 1 or bin(y + 1).count('1') == 1:
        return -1
    
    highest_bit = 1 << (y.bit_length() - 1)
    return highest_bit * 2 - 1 - y + (y & -y)

def main():
    t = int(input()) 
    for _ in range(t):
        x = int(input()) 
        print(solve(x))

if __name__ == "__main__":
    main()
