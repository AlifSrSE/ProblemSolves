# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1207/problem/C

def alif():
    t = int(input())
    
    for _ in range(t):
        n, a, b = map(int, input().split())
        s = input().strip()
        heights = [1] * (n + 1)

        for i in range(len(s)):
            if s[i] == '1':
                heights[i] = 2
                heights[i + 1] = 2
        begin_index = -1

        for i in range(len(heights)):
            if heights[i] == 2:
                if begin_index != -1:
                    end_index = i - 1
                    length = end_index - begin_index + 1
                    if length * b < 2 * a:
                        for j in range(begin_index, end_index + 1):
                            heights[j] = 2
                begin_index = i + 1
        height_changes = sum(1 for i in range(len(heights) - 1) if heights[i] != heights[i + 1])
        total_cost = (n + height_changes) * a + sum(heights) * b
        print(total_cost)

if __name__ == "__main__":
    alif()