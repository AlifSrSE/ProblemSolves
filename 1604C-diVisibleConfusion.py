# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def can_erase_sequence(a):
    for i in reversed(range(len(a))):
        if a[i] % (i + 2) != 0:
            continue
        else:
            return False
    return True

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print("YES" if can_erase_sequence(a) else "NO")

if __name__ == "__main__":
    main()