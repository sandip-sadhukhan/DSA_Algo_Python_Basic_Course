from collections import deque

queue = deque(["Sandip", "Hello", "Nice"])
print(queue)

queue.append("world")
print(queue)

queue.popleft()
print(queue)

print("-------")

# usinglist
q = [1, 2, 3, 4]
print(q)
q.append(5)
print(q)
q.pop(0)
print(q)
