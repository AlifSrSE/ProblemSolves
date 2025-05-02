# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1175/problem/B

LIMIT = (1 << 32) - 1

def alif(commands):
    stack = [(0, 0)] 
    for command in commands:
        if command.startswith("for"):
            loop = int(command.split(" ")[1])
            stack.append((loop, 0))
        elif command == "end":
            loop, amount = stack.pop()
            stack[-1] = (stack[-1][0], stack[-1][1] + loop * amount)
        else:
            stack[-1] = (stack[-1][0], stack[-1][1] + 1)

        if stack[-1][1] > LIMIT:
            return "OVERFLOW!!!"
    return str(stack[0][1])

if __name__ == "__main__":
    l = int(input())
    commands = [input() for _ in range(l)]
    print(alif(commands))