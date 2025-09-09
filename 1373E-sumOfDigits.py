# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def sum_digits(x):
    s = 0
    if x < 0:
        return float('inf')
    while x > 0:
        s += x % 10
        x //= 10
    return s

def get_smallest_number_with_sum(s):
    if s < 0:
        return -1
    if s == 0:
        return 0
    
    res_digits = []
    while s > 0:
        if s >= 9:
            res_digits.append(9)
            s -= 9
        else:
            res_digits.append(s)
            s = 0
    
    res = 0
    for digit in reversed(res_digits):
        res = res * 10 + digit
    return res

def get_smallest_number_with_sum_and_last_digit(s, d):
    if d > s or d < 0:
        return -1
    
    if d == 0 and s == 0:
        return 0
    
    rem_s = s - d
    prefix = get_smallest_number_with_sum(rem_s)
    
    if prefix == -1:
        return -1
        
    return prefix * 10 + d

def get_smallest_number_with_sum_not_ending_in_9(s):
    min_x = float('inf')
    for d in range(9):
        current_x = get_smallest_number_with_sum_and_last_digit(s, d)
        if current_x != -1:
            min_x = min(min_x, current_x)
    
    return min_x if min_x != float('inf') else -1

def alif():
    n, k = map(int, sys.stdin.readline().split())

    min_x = float('inf')
    
    for d in range(10):
        sum_last_digits_total = sum((d + i) % 10 for i in range(k + 1))
        rem_n = n - sum_last_digits_total
        
        num_terms_f_y = 10 - d
        if d + k < 10:
            num_terms_f_y = k + 1
        
        num_terms_f_y1 = (k + 1) - num_terms_f_y
        
        if num_terms_f_y1 == 0:
            if rem_n % num_terms_f_y == 0:
                target_f_y = rem_n // num_terms_f_y
                if target_f_y >= 0:
                    y_cand = get_smallest_number_with_sum(target_f_y)
                    if y_cand != -1:
                        x_cand = y_cand * 10 + d
                        
                        current_sum = 0
                        for i in range(k + 1):
                            current_sum += sum_digits(x_cand + i)
                        
                        if current_sum == n:
                            min_x = min(min_x, x_cand)
        else:
            for c in range(18):
                if c == 0:
                    if (rem_n - num_terms_f_y1) % (k + 1) == 0:
                        target_f_y = (rem_n - num_terms_f_y1) // (k + 1)
                        if target_f_y >= 0:
                            y_cand = get_smallest_number_with_sum_not_ending_in_9(target_f_y)
                            if y_cand != -1:
                                x_cand = y_cand * 10 + d
                                current_sum = 0
                                for i in range(k + 1):
                                    current_sum += sum_digits(x_cand + i)
                                if current_sum == n:
                                    min_x = min(min_x, x_cand)
                
                else:
                    if (rem_n - num_terms_f_y1 - num_terms_f_y * 9 * c) % (k + 1) == 0:
                        target_f_p = (rem_n - num_terms_f_y1 - num_terms_f_y * 9 * c) // (k + 1)
                        if target_f_p >= 0:
                            p_cand = get_smallest_number_with_sum_not_ending_in_9(target_f_p)
                            if p_cand != -1:
                                y_cand = int(str(p_cand) + '9' * c)
                                x_cand = y_cand * 10 + d
                                
                                current_sum = 0
                                for i in range(k + 1):
                                    current_sum += sum_digits(x_cand + i)
                                
                                if current_sum == n:
                                    min_x = min(min_x, x_cand)
                                
    if min_x == float('inf'):
        print(-1)
    else:
        print(min_x)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()
