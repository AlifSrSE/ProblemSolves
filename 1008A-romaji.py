# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(s):
    def is_vowel(letter):
        return letter in "aeiou"

    return all(is_vowel(s[i]) or s[i] == 'n' or (i + 1 < len(s) and is_vowel(s[i + 1])) for i in range(len(s)))

def main():
    s = input()
    print("YES" if solve(s) else "NO")

if __name__ == "__main__":
    main()