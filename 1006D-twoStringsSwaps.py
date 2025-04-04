# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def main():
    n = int(input())
    a = input().strip()
    b = input().strip()

    ans = 0

    for i in range(n // 2):
        st = set()
        st.add(a[i])
        st.add(a[n - i - 1])
        st.add(b[i])
        st.add(b[n - i - 1])

        if len(st) == 4:
            ans += 2
        elif len(st) == 3:
            if a[i] == a[n - i - 1] or b[i] == b[n - i - 1]:
                ans += 2
            else:
                ans += 1
        elif len(st) == 2:
            j = n - i - 1
            if (a[i] == a[j] and b[i] == b[j]) or \
               (a[i] == b[j] and b[i] == a[j]) or \
               (a[i] == b[i] and a[j] == b[j]):
                pass
            else:
                ans += 1

    if n % 2:
        if a[n // 2] != b[n // 2]:
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()
