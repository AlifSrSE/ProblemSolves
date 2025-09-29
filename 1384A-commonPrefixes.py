def alif():
    try:
        n = int(input())
    except EOFError:
        return
    
    s = ['a'] * 200
    print("".join(s))

    for _ in range(n):
        try:
            length_of_prev = int(input())
        except EOFError:
            break
            
        pos = length_of_prev
        
        if s[pos] == 'a':
            s[pos] = 'b'
        else:
            s[pos] = 'a'
        print("".join(s))

t = int(input())
for _ in range(t):
    alif()
