# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

BIT_NUM = 61

def find_bit(b_bit, c_bit, d_bit):
    for bit in range(2):
        if (bit | b_bit) - (bit & c_bit) == d_bit:
            return bit
    return -1

def solve(b, c, d):
    result = 0
    for i in range(BIT_NUM):
        b_bit = (b >> i) & 1
        c_bit = (c >> i) & 1
        d_bit = (d >> i) & 1
        bit = find_bit(b_bit, c_bit, d_bit)
        if bit == -1:
            return -1
        result += bit << i
    return result

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        b, c, d = map(int, input().split())
        print(solve(b, c, d))