# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

n = 8

array = [[True for _ in range(n)] for _ in range(n)]

pos1 = input()  
pos2 = input() 

rookRow = int(pos1[1]) - 1  
rookCol = ord(pos1[0]) - ord('a')  

for row in range(n):
    array[row][rookCol] = False
for col in range(n):
    array[rookRow][col] = False

knightRow = int(pos2[1]) - 1
knightCol = ord(pos2[0]) - ord('a')
array[knightRow][knightCol] = False

for row in range(1, 3):
    for col in range(1, 3):
        if row + col != 3:  
            continue
            
        posRow = knightRow + row
        posCol = knightCol + col
        if posRow < n and posCol < n:
            array[posRow][posCol] = False

        posRow = knightRow - row
        posCol = knightCol + col
        if posRow >= 0 and posCol < n:
            array[posRow][posCol] = False

        posRow = knightRow + row
        posCol = knightCol - col
        if posRow < n and posCol >= 0:
            array[posRow][posCol] = False

        posRow = knightRow - row
        posCol = knightCol - col
        if posRow >= 0 and posCol >= 0:
            array[posRow][posCol] = False

        posRow = rookRow + row
        posCol = rookCol + col
        if posRow < n and posCol < n:
            array[posRow][posCol] = False

        posRow = rookRow - row
        posCol = rookCol + col
        if posRow >= 0 and posCol < n:
            array[posRow][posCol] = False

        posRow = rookRow + row
        posCol = rookCol - col
        if posRow < n and posCol >= 0:
            array[posRow][posCol] = False

        posRow = rookRow - row
        posCol = rookCol - col
        if posRow >= 0 and posCol >= 0:
            array[posRow][posCol] = False

total = 0
for row in range(n):
    for col in range(n):
        total += 1 if array[row][col] else 0 

print(total)