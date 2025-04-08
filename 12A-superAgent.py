# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def main():
    N = 3 * 3
    buttons = [False] * N
    
    k = 0
    for _ in range(3):  
        input_str = input()
        for temp in input_str:
            if k >= N:
                break
            if temp == 'X':
                buttons[k] = True
                k += 1
            elif temp == '.':
                buttons[k] = False
                k += 1
    
    symmetric = True
    for k in range(N):
        if buttons[k] != buttons[N - 1 - k]:
            symmetric = False
            break
    
    if symmetric:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()