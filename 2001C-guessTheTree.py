# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

from collections import deque

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        adj = [[] for _ in range(n + 1)] 
        edges = [] 
        
        for i in range(2, n + 1):
            print(f"? 1 {i}", flush=True)
            x = int(input())
            if x == 1:
                edges.append((1, i))
            else:
                print(f"? {x} {i}", flush=True)
                y = int(input())
                if y == x:
                    edges.append((x, i))
                else:
                    edges.append((x, i))
        
        print("! ", end="", flush=True)
        for a, b in edges:
            print(f"{a} {b} ", end="", flush=True)
        print(flush=True)

if __name__ == "__main__":
    main()