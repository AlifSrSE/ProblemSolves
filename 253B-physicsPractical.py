# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(c):
    c.sort()
    result = float('inf')
    end_index = 0

    for i in range(len(c)):
        while end_index != len(c) - 1 and c[end_index + 1] <= 2 * c[i]:
            end_index += 1

        result = min(result, len(c) - (end_index - i + 1))

    return result


def main():
    with open("input.txt", "r") as infile:
        n = int(infile.readline())
        c = list(map(int, infile.readline().split()))

    result = solve(c)

    with open("output.txt", "w") as outfile:
        outfile.write(str(result) + "\n")


if __name__ == "__main__":
    main()
