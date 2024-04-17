from collections import deque
#adding elements in deques
q= deque()
q.append(10)
q.append(100)
q.append(1000)
q.append(10000)
print(q)
#removing elements from deques
q.pop()
print(q)

q.count(1)
print(q)
#implementation  using queue, Queue
from queue import Queue
a=Queue(maxsize=4)
print(a.qsize())
a.put("Book")
a.put("pen")
a.put("pencil")
a.put("school")
print(a.full())
print(a.get())
print(a.get())
print(a.get())
print(a.empty())
