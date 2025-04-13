# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def main():
    test_cases = int(input())
    
    for _ in range(test_cases):
        words = input().split()
        initials = ''.join(word[0] for word in words)
        print(initials)

if __name__ == "__main__":
    main()
