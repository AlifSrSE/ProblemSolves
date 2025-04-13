# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(line):
    alphabet_length = 26
    letters = [False] * alphabet_length
    for char in line:
        if 'a' <= char <= 'z':
            letters[ord(char) - ord('a')] = True
    output = sum(letters)
    return "IGNORE HIM!" if output % 2 else "CHAT WITH HER!"

if __name__ == "__main__":
    line = input()
    print(solve(line))