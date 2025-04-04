# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(n, a):
    type_to_count = {}
    for type_val in a:
        type_to_count[type_val] = type_to_count.get(type_val, 0) + 1
    
    day = len(a) // n
    while day >= 0:
        if compute_people_num(type_to_count, day) >= n or day == 0:
            return day
        day -= 1

def compute_people_num(type_to_count, day):
    if day == 0:
        return float('inf')
    return sum(count // day for count in type_to_count.values())

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, a))

if __name__ == "__main__":
    main()