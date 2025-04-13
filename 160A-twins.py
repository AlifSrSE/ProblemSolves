# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    num_coins = int(data[0])
    coins = list(map(int, data[1:num_coins + 1]))
    total = sum(coins)
    coins.sort()
    
    output_coins = 0
    output_value = 0
    while output_value <= total // 2:
        output_coins += 1
        output_value += coins[num_coins - output_coins]
    
    print(output_coins)

if __name__ == "__main__":
    main()