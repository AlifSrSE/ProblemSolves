# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    num_boys, num_girls = map(int, input_file.readline().split())
    comm = diff = 0
    min_char = max_char = ''
    
    if num_boys > num_girls:
        comm = num_girls
        diff = num_boys - num_girls
        max_char = 'B'
        min_char = 'G'
    else:
        comm = num_boys
        diff = num_girls - num_boys
        max_char = 'G'
        min_char = 'B'
    
    output_file.write(f"{max_char}{min_char}" * comm)
    output_file.write(f"{max_char}" * diff)
    output_file.write("\n")