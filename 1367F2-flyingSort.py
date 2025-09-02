import sys
import bisect

def alif():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = sorted(a)
    a_pos = {}

    for i, val in enumerate(a):
        if val not in a_pos:
            a_pos[val] = []
        a_pos[val].append(i)
    dp_state = [(0, 0)] * n
    max_len = 0
    
    for i in range(n):
        cur_val = b[i]
        cur_pos_list = a_pos[cur_val]
        can_extend = False
        
        if i > 0:
            prev_val = b[i-1]
            prev_len, prev_last_idx = dp_state[i-1]
            idx_in_cur_list = bisect.bisect_right(cur_pos_list, prev_last_idx)
            
            if idx_in_cur_list < len(cur_pos_list):
                last_idx_cur = cur_pos_list[idx_in_cur_list]
                if cur_val == prev_val and last_idx_cur <= prev_last_idx:
                    dp_state[i] = (1, cur_pos_list[0])
                else:
                    dp_state[i] = (prev_len + 1, last_idx_cur)
                can_extend = True
        
        if not can_extend:
            last_idx_cur = cur_pos_list[0]
            dp_state[i] = (1, last_idx_cur)
        max_len = max(max_len, dp_state[i][0])
    print(n - max_len)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()