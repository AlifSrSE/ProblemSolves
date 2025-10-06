# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    data_index = 0
    t = int(input_data[data_index])
    data_index += 1
    results = []
    
    for _ in range(t):
        n = int(input_data[data_index])
        data_index += 1
        s = input_data[data_index]
        data_index += 1
        m = {}
        m[0] = 1
        cs = 0
        ans = 0
        
        for p in range(len(s)):
            digit = int(s[p])
            cs += digit
            cur = cs - (p + 1)
            
            if cur in m:
                m[cur] += 1
            else:
                m[cur] = 1
                
            ans += m[cur] - 1

        results.append(str(ans))

    sys.stdout.write('\n'.join(results) + '\n')

alif()
