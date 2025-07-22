# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/2125/problem/A

def alif():
    si = input()
    cTI = si.count('T')
    cFI = si.count('F')
    cNI = si.count('N')
    
    oith = [ch for ch in si if ch not in {'T', 'F', 'N'}]
    print('T' * cTI + 'F' * cFI + 'N' * cNI + ''.join(oith))


def main():
    ti = int(input())
    for _ in range(ti):
        alif()

if __name__ == "__main__":
    main()