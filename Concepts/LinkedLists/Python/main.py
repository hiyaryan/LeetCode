from LinkedList import LinkedList
from Node import Node

# Adding one node at a time to an empty LL.
llist = LinkedList()
print(llist)

first_node = Node("a")
llist.head = first_node
print(llist)

second_node = Node("b")
third_node = Node("c")

first_node.next = second_node
second_node.next = third_node
print(llist)

# Creating a new LL with initial values.
llist = LinkedList(["a", "b", "c", "d", "e"])
print(llist)

# Using the iterable in the LinkedList class.
for node in llist:
    print(node)

