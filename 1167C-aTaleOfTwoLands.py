# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1167/problem/C

def find_max_index_with_less_equal(sorted_arr, target):
    result = -1
    lower_index = 0
    upper_index = len(sorted_arr) - 1
    while lower_index <= upper_index:
        middle_index = (lower_index + upper_index) // 2
        if sorted_arr[middle_index] <= target:
            result = middle_index
            lower_index = middle_index + 1
        else:
            upper_index = middle_index - 1
    return result

def alif(a):
    sorted_arr = sorted(abs(x) for x in a)
    return sum(find_max_index_with_less_equal(sorted_arr, sorted_arr[i] * 2) - i 
               for i in range(len(sorted_arr)))

n = int(input())
a = list(map(int, input().split()))
print(alif(a))