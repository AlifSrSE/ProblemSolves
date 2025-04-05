# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    zeros_count = a.count(0)
    present_numbers = sorted([x for x in a if x != 0])
    missing_numbers = sorted(list(set(range(1, n + 1)) - set(present_numbers)))

    if zeros_count == 0:
        def calculate_f(arr):
            m = len(arr)
            if m == 1:
                return arr[0]

            memo = {}

            def get_f_recursive(current_arr, turn):
                current_tuple = (tuple(current_arr), turn)
                if current_tuple in memo:
                    return memo[current_tuple]

                m_current = len(current_arr)
                if m_current == 1:
                    return current_arr[0]

                results = []
                for i in range(m_current - 1):
                    next_arr = list(current_arr)
                    val1 = next_arr[i]
                    val2 = next_arr[i + 1]
                    del next_arr[i + 1]
                    if turn == 0:  # Turtle's turn
                        next_arr[i] = min(val1, val2)
                        results.append(get_f_recursive(tuple(next_arr), 1))
                    else:  # Piggy's turn
                        next_arr[i] = max(val1, val2)
                        results.append(get_f_recursive(tuple(next_arr), 0))

                if turn == 0:
                    result = max(results)
                else:
                    result = min(results)
                memo[current_tuple] = result
                return result

            return get_f_recursive(tuple(arr), 0)

        total_beauty = 0
        for i in range(n):
            for j in range(i, n):
                subsegment = a[i : j + 1]
                total_beauty += calculate_f(subsegment)
        print(total_beauty)
        return

    def calculate_f_optimized(arr):
        m = len(arr)
        if m == 1:
            return arr[0]
        return arr[0] if m % 2 == 1 else min(arr[0], arr[-1])

    def calculate_beauty(perm):
        beauty = 0
        for i in range(n):
            for j in range(i, n):
                subsegment = perm[i : j + 1]
                beauty += calculate_f_optimized(subsegment)
        return beauty

    import itertools

    max_beauty = 0
    possible_fills = list(itertools.permutations(missing_numbers))

    for fill in possible_fills:
        temp_perm = list(a)
        fill_idx = 0
        for i in range(n):
            if temp_perm[i] == 0:
                temp_perm[i] = fill[fill_idx]
                fill_idx += 1
        max_beauty = max(max_beauty, calculate_beauty(temp_perm))

    print(max_beauty)


t = int(input())
for _ in range(t):
    solve()