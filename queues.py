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

# FIFO Principle
import queue
queu_1 = queue.Queue()
queu_1.put(10)
queu_1.put("Mercy")
queu_1.put(20.3)
queu_1.put("Banana")
#Removing elements from a queue
print(queu_1.get())
print(queu_1.get())
print(type(queu_1))
#LIFO Principle
import queue
queue_2 = queue.LifoQueue()
queue_2.put("mother")
queue_2.put("father")
queue_2.put("children")
queue_2.put("family")
print(queue_2.get())
print(queue_2.get())
print(queue_2.get())
print(type(queue_2))
 #Priority Queue Method
import queue
queue_3 = queue.PriorityQueue()
queue_3.put((4,""))
queue_3.put((5,"Maserati"))
queue_3.put((2,"Macedes"))
queue_3.put((1, "BMW"))
queue_3.put((3, "Subaru"))
print(queue_3.get())
print(queue_3.get())
print(type(queue_3))
