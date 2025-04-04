# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

class Student:
    def __init__(self, id, a, b, c, d):
        self.id = id
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def get_sum(self):
        return self.a + self.b + self.c + self.d

def solve():
    n = int(input())
    students = []
    
    for i in range(n):
        a, b, c, d = map(int, input().split())
        students.append(Student(i + 1, a, b, c, d))
    
    students.sort(key=lambda x: (-x.get_sum(), x.id))
    
    for i in range(n):
        if students[i].id == 1:
            return i + 1

print(solve())