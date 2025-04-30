# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1159/problem/B

def alif():
    n = int(input())
    a = list(map(int, input().split()))

    def is_k_extension(arr, k):
        n_arr = len(arr)
        for i in range(n_arr):
            for j in range(n_arr):
                if k * abs(i - j) > min(arr[i], arr[j]):
                    return False
        return True

    low = 0
    high = 10**9 + 1

    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if is_k_extension(a, mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    print(ans)

if __name__ == "__main__":
    alif()