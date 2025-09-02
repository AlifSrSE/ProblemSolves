# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

from collections import defaultdict
import heapq

def alif():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    topics = list(map(int, input().split()))
    topics = [t - 1 for t in topics]
    topic_to_blogs = defaultdict(list)

    for blog in range(1, n + 1):
        topic_to_blogs[topics[blog - 1]].append(blog)
    
    written = set()
    order = []
    heap = []
    for topic in range(n):
        for blog in topic_to_blogs[topic]:
            heapq.heappush(heap, (topic, blog))
    
    while heap:
        topic, blog = heapq.heappop(heap)
        neighbor_topics = set()
        for neighbor in graph[blog]:
            if neighbor in written:
                neighbor_topic = topics[neighbor - 1]
                neighbor_topics.add(neighbor_topic)
        mex = 0

        while mex in neighbor_topics:
            mex += 1
        
        if mex != topic:
            return [-1]
        
        order.append(blog)
        written.add(blog)
    
    if len(order) != n:
        return [-1]
    return order

result = alif()
if result == [-1]:
    print(-1)
else:
    print(*result)