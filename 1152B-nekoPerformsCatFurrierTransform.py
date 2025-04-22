# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1152/problem/B

def alif(x):
    exponents = []

    while True:
        binary = bin(x)[2:]
        first_zero_index = binary.find('0')

        
        if first_zero_index == -1:
            break

        exponent = len(binary) - first_zero_index
        if int(binary[first_zero_index:], 2) == 0:
            exponent -= 1

        exponents.append(exponent)

        x ^= (1 << exponent) - 1
        x += 1

    return f"{len(exponents) * 2}\n{' '.join(map(str, exponents))}"

if __name__ == "__main__":
    x = int(input())
    print(alif(x))
