# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a):
    value_to_count = {}
    for value in a:
        value_to_count[value] = value_to_count.get(value, 0) + 1

    count = 0
    for x in a:
        found = False
        for i in range(1, 32):
            other = (1 << i) - x
            if other == x:
                if value_to_count.get(x, 0) >= 2:
                    found = True
                    break
            elif other in value_to_count:
                found = True
                break
        if found:
            count += 1
    return len(a) - count

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))

if __name__ == "__main__":
    main()