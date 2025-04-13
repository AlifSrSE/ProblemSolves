# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(ticket):
    half_len = len(ticket) // 2
    sorted_left = sorted(int(c) for c in ticket[:half_len])
    sorted_right = sorted(int(c) for c in ticket[half_len:])

    return all(sorted_left[i] < sorted_right[i] for i in range(half_len)) or \
           all(sorted_left[i] > sorted_right[i] for i in range(half_len))

if __name__ == "__main__":
    input() 
    ticket = input()
    print("YES" if solve(ticket) else "NO")