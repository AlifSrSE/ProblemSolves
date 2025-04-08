# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

initial_price, max_reduction = map(int, input().split())

mod_num = 10
final_price = initial_price

while True:
    tail = initial_price % mod_num
    test_reduction = (tail + 1) % mod_num

    if test_reduction > max_reduction:
        break

    final_price = initial_price - test_reduction
    mod_num *= 10

print(final_price)