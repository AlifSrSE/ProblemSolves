# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def main():
    input_str = input()
    if not input_str:
        print("")
        return

    output = input_str[0]
    total = 1

    if len(input_str) >= 2:
        output += input_str[1]
        total += 1

    for k in range(2, len(input_str)):
        if input_str[k - 1] == input_str[k] and input_str[k - 2] == input_str[k]:
            continue
        elif input_str[k - 1] == input_str[k] and output[total - 3] == output[total - 2]:
            continue
        output += input_str[k]
        total += 1

    print(output)

if __name__ == "__main__":
    main()
