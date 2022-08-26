from collections import deque

# LINKED LISTS (collections module)
a = deque(['a', 'b', 'c'])
print("a =", a)

b = deque([{'data', 'a'}, {'data', 'b'}])
print("b =", b)

# may pass any iterable as an input for deque
c = deque("abcde")
print("c =", c)

# append to the end of the list
c.append("f")
print("c.append('f') = ", c)

# pop the tail
c.pop()
print("c.pop() = ", c)

d = deque(['z', 'a', 'b', 'c', 'd', 'e'])
print("d =", d)

# pop the head
d.popleft()
print("d.popleft", d)


# QUEUES
queue = deque()
print("queue =", queue)

# use append and popleft function to replicate a queue
queue.append("Mary")
print("queue.append('Mary') =", queue)

queue.append("John")
print("queue.append('John') =", queue)

queue.append("Susan")
print("queue.append('Susan') =", queue)

queue.popleft()
print("queue.popleft() =", queue)

queue.popleft()
print("queue.popleft() =", queue)


# STACKS
history = deque()
print("history =", history)

# use appendleft and popleft functions to replicate a stack
history.appendleft("index")
print("history.appendleft('index') =", history)

history.appendleft("index/home")
print("history.appendleft('index/home') =", history)

history.appendleft("index/home/contents")
print("history.appendleft('index/home/contents') =", history)

history.popleft()
print("history.popleft() =", history)

history.popleft()
print("history.popleft() =", history)
