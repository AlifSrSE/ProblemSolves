# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1156/problem/B

def alif():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        n = len(s)
        odd = []
        even = []
        mp = {}
        
        for ch in s:
            if (ord(ch) - ord('a')) % 2 == 0:
                if ch not in mp:
                    odd.append(ch)
                mp[ch] = mp.get(ch, 0) + 1
            else:
                if ch not in mp:
                    even.append(ch)
                mp[ch] = mp.get(ch, 0) + 1
        
        odd.sort()
        even.sort()
        
        if not even:
            for ch in odd:
                print(ch * mp[ch], end='')
            print()
        
        elif not odd:
            for ch in even:
                print(ch * mp[ch], end='')
            print()
        
        else:
            if abs(ord(odd[-1]) - ord(even[0])) == 1:
                if abs(ord(even[-1]) - ord(odd[0])) == 1:
                    print("No answer")
                    continue
                else:
                    for ch in even:
                        print(ch * mp[ch], end='')
                    for ch in odd:
                        print(ch * mp[ch], end='')
                    print()
            else:
                for ch in odd:
                    print(ch * mp[ch], end='')
                for ch in even:
                    print(ch * mp[ch], end='')
                print()

if __name__ == "__main__":
    alif()