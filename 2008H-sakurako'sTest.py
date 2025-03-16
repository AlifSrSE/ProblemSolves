# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/2008/problem/H

def process_test_case():
    num_elements, num_queries = map(int, input().split())
    element_array = list(map(int, input().split()))
    frequency_sums = [0] * (num_elements + 1)
    
    for element in element_array:
        frequency_sums[element] += 1
    
    for index in range(1, num_elements + 1):
        frequency_sums[index] += frequency_sums[index - 1]
    
    result_array = [0] * (num_elements + 1)
    
    for size in range(1, num_elements + 1):
        left_bound, right_bound = 0, size
        while left_bound < right_bound:
            middle_point = (left_bound + right_bound) // 2
            total_count = frequency_sums[middle_point]
            for multiple in range(1, num_elements // size + 1):
                total_count += frequency_sums[min(multiple * size + middle_point, num_elements)] - frequency_sums[multiple * size - 1]
            if total_count - 1 >= num_elements // 2:
                right_bound = middle_point
            else:
                left_bound = middle_point + 1
        result_array[size] = left_bound
    
    query_results = []
    for _ in range(num_queries):
        query_value = int(input())
        query_results.append(result_array[query_value])
    print(*query_results)

num_test_cases = int(input())
for _ in range(num_test_cases):
    process_test_case()