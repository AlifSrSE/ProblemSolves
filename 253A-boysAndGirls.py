# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(num_boys, num_girls):
    result = []
    while num_boys > 0 or num_girls > 0:
        if num_boys > num_girls:
            if len(result) == 0 or result[-1] != 'B':
                result.append('B')
                num_boys -= 1
            else:
                if num_girls > 0:
                    result.append('G')
                    num_girls -= 1
                else:
                    result.append('B')
                    num_boys -= 1
        else:
            if len(result) == 0 or result[-1] != 'G':
                result.append('G')
                num_girls -= 1
            else:
                if num_boys > 0:
                    result.append('B')
                    num_boys -= 1
                else:
                    result.append('G')
                    num_girls -= 1
    return ''.join(result)

if __name__ == "__main__":
    num_boys, num_girls = map(int, input().split())
    print(solve(num_boys, num_girls))