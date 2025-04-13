# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys

def query(t):
    print(f"? {t}", flush=True)
    return int(sys.stdin.readline()) == 1

def respond(s):
    print(f"! {s}", flush=True)

def proceed(n, t):
    while len(t) != n:
        if query(t + "0"):
            t += "0"
        elif query(t + "1"):
            t += "1"
        else:
            break
    
    while len(t) != n:
        if query("0" + t):
            t = "0" + t
        else:
            t = "1" + t
    
    respond(t)

def main():
    input = sys.stdin.read
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n == 1:
            if query("0"):
                respond("0")
            else:
                respond("1")
        elif query("01"):
            proceed(n, "01")
        elif query("10"):
            proceed(n, "10")
        elif query("0"):
            respond("0" * n)
        else:
            respond("1" * n)

if __name__ == "__main__":
    main()