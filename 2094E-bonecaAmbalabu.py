# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def main():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        bit_counts = [0] * 30  
        
        for num in a:
            for b in range(30):
                if num & (1 << b):
                    bit_counts[b] += 1
        
        max_sum = 0
        
        for num in a:
            total = 0
            for b in range(30):
                if num & (1 << b):
                    total += (n - bit_counts[b]) * (1 << b)
                else:
                    total += bit_counts[b] * (1 << b)
            max_sum = max(max_sum, total)
        
        print(max_sum)

if __name__ == "__main__":
    main()
