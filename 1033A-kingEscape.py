# Author : AlifSrSE
# Date : 2025-02-16
# Problem link : https://codeforces.com/contest/1033/problem/A

def is_same_quadrant(ax, ay, bx, by, cx, cy):
 return (bx < ax and cx < ax and by < ay and cy < ay) or \
           (bx < ax and cx < ax and by > ay and cy > ay) or \
           (bx > ax and cx > ax and by < ay and cy < ay) or \
           (bx > ax and cx > ax and by > ay and cy > ay)
def can_bob_win(n, ax, ay, bx, by, cx, cy):
    if is_same_quadrant(ax, ay, bx, by, cx, cy):
        return "YES"
    else:
       return "NO"
    
n = int(input().strip())
ax, ay = map(int, input().strip().split())
bx, by = map(int, input().strip().split())
cx, cy = map(int, input().strip().split())

result = can_bob_win(n, ax, ay, bx, by, cx, cy)
print(result)