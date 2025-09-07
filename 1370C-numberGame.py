# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        
        if n == 1:
            print("FastestFinger")
            continue
        if n == 2:
            print("Ashishgup")
            continue
        if n % 2 == 1:
            print("Ashishgup")
            continue
        
        count_twos = 0
        temp_n = n
        while temp_n % 2 == 0:
            temp_n //= 2
            count_twos += 1
        
        if temp_n == 1:
            print("FastestFinger")
            continue
        
        if count_twos == 1:
            is_prime = True
            for i in range(2, int(temp_n**0.5) + 1):
                if temp_n % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print("FastestFinger")
            else:
                print("Ashishgup")
        else:
            print("Ashishgup")

if __name__ == '__main__':
    main()
