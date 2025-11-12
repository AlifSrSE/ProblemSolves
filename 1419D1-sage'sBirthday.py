import sys
def alif():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    data_idx = 1
    
    if n == 0:
        sys.stdout.write("0\n\n")
        return
        
    a = [int(data[data_idx + i]) for i in range(n)]
    a.sort()
    
    small = a[:n//2]
    large = a[n//2:]
    result = []
    
    for i in range(n):
        if i % 2 == 0:
            result.append(large.pop(0))
        else:
            result.append(small.pop(0))
            
    sys.stdout.write(f"{(n - 1) // 2}\n")
    sys.stdout.write(" ".join(map(str, result)) + "\n")
alif()