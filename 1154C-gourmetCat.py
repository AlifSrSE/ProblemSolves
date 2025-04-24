# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1154/problem/C

def alif(a, b, c):
    cycle = min(a // 3, b // 2, c // 2)

    def compute_day_num(remain_a, remain_b, remain_c, start_day):
        result = 0
        day = start_day
        while True:
            if day in [1, 4, 7]:
                if remain_a == 0:
                    break
                remain_a -= 1
            elif day in [2, 6]:
                if remain_b == 0:
                    break
                remain_b -= 1
            else:
                if remain_c == 0:
                    break
                remain_c -= 1

            result += 1
            day = day % 7 + 1
        return result

    max_extra_days = max(
        compute_day_num(a - cycle * 3, b - cycle * 2, c - cycle * 2, start_day)
        for start_day in range(1, 8)
    )

    return cycle * 7 + max_extra_days

if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(alif(a, b, c))
