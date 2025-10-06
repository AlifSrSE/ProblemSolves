# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
def alif():
    t = int(input())
    
    for _ in range(t):
        p, f = map(int, input().split())
        cnt_s, cnt_w = map(int, input().split())
        s, w = map(int, input().split())
        
        if s > w:
            s, w = w, s
            cnt_s, cnt_w = cnt_w, cnt_s
        total = 0

        for swords_you in range(cnt_s + 1):
            if swords_you * s > p:
                break
            axes_you = min(cnt_w, (p - swords_you * s) // w)
            swords_left = cnt_s - swords_you
            axes_left = cnt_w - axes_you
            swords_follower = min(swords_left, f // s)
            axes_follower = min(axes_left, (f - swords_follower * s) // w)
            total = max(total, swords_you + axes_you + swords_follower + axes_follower)
        
        print(total)

alif()