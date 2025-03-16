# Author : AlifSrSE
# Date : 2025-03-15
# Problem link : https://codeforces.com/contest/1213/problem/A
 
def main():
    n = int(input())
    even = 0
    odd = 0
    numbers = list(map(int, input().split()))
    
    for x in numbers:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    
    print(min(even, odd))
 
if __name__ == "__main__":
    main()