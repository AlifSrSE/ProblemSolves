# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1263/problem/B

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        pv = []
        pset = set()
        cnt = 0

        initial_pins = []
        for _ in range(n):
            initial_pins.append(sys.stdin.readline().strip())

        for p_idx in range(n):
            s = initial_pins[p_idx]

            if s in pset:
                cnt += 1
                done_modifying = False

                for digit_pos in range(len(s)):
                    if done_modifying:
                        break
                    
                    original_digit_char = s[digit_pos]
                    original_digit_val = int(original_digit_char)

                    for new_digit_val in range(10):
                        if done_modifying:
                            break
                        
                        if original_digit_val == new_digit_val:
                            continue
                        
                        temp_s_list = list(s) 
                        temp_s_list[digit_pos] = str(new_digit_val)
                        t = "".join(temp_s_list)

                        if t not in pset:
                            s = t
                            done_modifying = True 
                            break
            pv.append(s)
            pset.add(s) 

        sys.stdout.write(f"{cnt}\n")
        for pin in pv:
            sys.stdout.write(f"{pin}\n")

if __name__ == "__main__":
    alif()