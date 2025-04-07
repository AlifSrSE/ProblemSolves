# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def main():
    n = int(input())
    object_arr = [False] * n
    previous = [0] * n
    out_degree = [0] * n

    hotels = []
    temp_values = list(map(int, input().split()))
    for k in range(n):
        object_arr[k] = bool(temp_values[k])
        if object_arr[k]:
            hotels.append(k)

    temp_values = list(map(int, input().split()))
    for k in range(n):
        temp = temp_values[k]
        if temp == 0:
            previous[k] = -1
        else:
            previous[k] = temp - 1
            out_degree[temp - 1] += 1

    best_path = []
    for hotel in hotels:
        current_path = [hotel]
        current = previous[hotel]
        while current >= 0 and not object_arr[current] and out_degree[current] <= 1:
            current_path.append(current)
            current = previous[current]
        if len(current_path) > len(best_path):
            best_path = current_path

    print(len(best_path))
    print(' '.join(str(x + 1) for x in reversed(best_path)))

if __name__ == "__main__":
    main()
