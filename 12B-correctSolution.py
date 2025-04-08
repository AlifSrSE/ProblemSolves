# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def main():
    input_str = input()  
    answer = input()   
    
    count = [0] * 10
    min_non_zero = 'A' 
    
    for char in input_str:
        digit = int(char)   
        count[digit] += 1
        if char > '0' and char < min_non_zero:
            min_non_zero = char

    output = ""
    if min_non_zero == 'A':    
        output = "0"
    else:
        count[int(min_non_zero)] -= 1  
        output += min_non_zero
        for digit in range(10):
            while count[digit] > 0:
                output += str(digit)
                count[digit] -= 1
    
    if answer == output:
        print("OK")
    else:
        print("WRONG_ANSWER")

if __name__ == "__main__":
    main()