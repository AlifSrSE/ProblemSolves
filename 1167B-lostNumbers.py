# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1167/problem/B

import sys

class Query:
    def __init__(self, index1, index2):
        self.index1 = index1
        self.index2 = index2
        self.answer = 0

def swap(a, index1, index2):
    a[index1], a[index2] = a[index2], a[index1]

def search(queries, a, index):
    if index == len(a):
        if all(a[q.index1] * a[q.index2] == q.answer for q in queries):
            print(f"! {' '.join(map(str, a))}", flush=True)
        return
    
    for i in range(index, len(a)):
        swap(a, i, index)
        search(queries, a, index + 1)
        swap(a, i, index)

def alif():
    queries = [Query(0, 1), Query(1, 2), Query(2, 3), Query(3, 4)]
    for q in queries:
        print(f"? {q.index1 + 1} {q.index2 + 1}", flush=True)
        q.answer = int(input())
    
    a = [4, 8, 15, 16, 23, 42]
    search(queries, a, 0)

alif()