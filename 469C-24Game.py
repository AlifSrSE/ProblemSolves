# Author : AlifSrSE
# Date : 2025-03-10
# Problem link : https://codeforces.com/contest/469/problem/C

def solve_24_game(n):
    if n < 4:
        print("NO")
        return

    print("YES")
    operations = []

    if n == 4:
        operations.append("1 * 2 = 2")
        operations.append("2 * 3 = 6")
        operations.append("6 * 4 = 24")
    elif n == 5:
        operations.append("1 + 2 = 3")
        operations.append("3 + 3 = 6")
        operations.append("6 * 4 = 24")
        operations.append("24 + 5 = 29")
        operations.append("29 - 5 = 24")
    else:
        stack = list(range(1, n + 1))
        while len(stack) > 4:
            a, b = stack.pop(), stack.pop()
            operations.append(f"{a} - {b} = {a - b}")
            stack.append(a - b)

        a, b, c, d = stack.pop(), stack.pop(), stack.pop(), stack.pop()
        operations.append(f"{d} * {c} = {d * c}")
        operations.append(f"{b} * {a} = {b * a}")
        
        a,b,c,d = a,b,c,d
        
        operations.append(f"{b-2} - {b-3} = -1")
        operations.append(f"{b-4} - {b-5} = -1")
        operations.append(f"{a*b} - {d*c} = {a*b-d*c}")
        operations.append(f"{a*b-d*c} - {-1} = {a*b-d*c+1}")
        operations.append(f"{a*b-d*c+1} + {-1} = 24")
        
        if n == 8:
            operations = []
            operations.append(f"{8} * {7} = {56}")
            operations.append(f"{6} * {5} = {30}")
            operations.append(f"{3} - {4} = {-1}")
            operations.append(f"{1} - {2} = {-1}")
            operations.append(f"{30} - {-1} = {31}")
            operations.append(f"{56} - {31} = {25}")
            operations.append(f"{25} + {-1} = {24}")
        elif n%2 == 0:
            operations = []
            operations.append(f"{n} * {n-1} = {n*(n-1)}")
            operations.append(f"{n-2} * {n-3} = {(n-2)*(n-3)}")
            operations.append(f"{3} - {4} = {-1}")
            operations.append(f"{1} - {2} = {-1}")
            operations.append(f"{(n-2)*(n-3)} - {-1} = {(n-2)*(n-3)+1}")
            operations.append(f"{n*(n-1)} - {(n-2)*(n-3)+1} = {n*(n-1)-((n-2)*(n-3)+1)}")
            operations.append(f"{n*(n-1)-((n-2)*(n-3)+1)} + {-1} = {24}")
        else:
            operations = []
            operations.append(f"{n} * {n-1} = {n*(n-1)}")
            operations.append(f"{n-2} * {n-3} = {(n-2)*(n-3)}")
            operations.append(f"{3} + {4} = {7}")
            operations.append(f"{1} + {2} = {3}")
            operations.append(f"{(n-2)*(n-3)} - {3} = {(n-2)*(n-3)-3}")
            operations.append(f"{n*(n-1)} - {(n-2)*(n-3)-3} = {n*(n-1)-((n-2)*(n-3)-3)}")
            operations.append(f"{n*(n-1)-((n-2)*(n-3)-3)} - {7} = {24}")
        

    for op in operations:
        print(op)

n = int(input().strip())
solve_24_game(n)