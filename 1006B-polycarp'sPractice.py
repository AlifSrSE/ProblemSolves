# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

class Element:
    def __init__(self, index, value):
        self.index = index
        self.value = value

def solve(a, k):
    elements = [Element(i, a[i]) for i in range(len(a))]
    sorted_elements = sorted(sorted(elements, key=lambda x: x.index), key=lambda x: x.value, reverse=True)[:k]
    total_profit = sum(element.value for element in sorted_elements)

    counts = []
    if len(sorted_elements) == 1:
        counts.append(len(a))
    else:
        counts.append(sorted_elements[1].index)
        for i in range(1, len(sorted_elements)):
            counts.append((len(a) if i == len(sorted_elements) - 1 else sorted_elements[i + 1].index) - sorted_elements[i].index)

    return f"{total_profit}\n{' '.join(map(str, counts))}"

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(a, k))

if __name__ == "__main__":
    main()