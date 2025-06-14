# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1208/problem/B

def alif():
    n = int(input())
    a = list(map(int, input().split()))
    max_size = 0
    left_set = set()
    
    for left_length in range(n + 1):
        right_set = set()
        for j in range(n - 1, left_length - 1, -1):
            if a[j] in left_set or a[j] in right_set:
                break
            right_set.add(a[j])
        max_size = max(max_size, len(left_set) + len(right_set))
        
        if left_length < n:
            if a[left_length] in left_set:
                break
            left_set.add(a[left_length])
    print(n - max_size)

if __name__ == "__main__":
    alif()