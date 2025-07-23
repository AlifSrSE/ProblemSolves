# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1251/problem/D

import sys

def alif():
    q = int(sys.stdin.readline())

    for _ in range(q):
        s = sys.stdin.readline().strip()
        
        x_chars = []
        y_chars = []
        
        for char_s in s:
            if (ord(char_s) - ord('a')) % 2 != 0:
                x_chars.append(char_s)
            else:
                y_chars.append(char_s)
        
        merged_result = []
        ptr_x = 0
        ptr_y = 0

        while ptr_x < len(x_chars) or ptr_y < len(y_chars):
            if ptr_x < len(x_chars) and ptr_y < len(y_chars):
                if x_chars[ptr_x] < y_chars[ptr_y]:
                    merged_result.append(x_chars[ptr_x])
                    ptr_x += 1
                else:
                    merged_result.append(y_chars[ptr_y])
                    ptr_y += 1
            elif ptr_x < len(x_chars):
                merged_result.append(x_chars[ptr_x])
                ptr_x += 1
            elif ptr_y < len(y_chars):
                merged_result.append(y_chars[ptr_y])
                ptr_y += 1
        
        sys.stdout.write("".join(merged_result) + "\n")

if __name__ == "__main__":
    alif()