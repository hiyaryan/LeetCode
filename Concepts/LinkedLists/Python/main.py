from LinkedList import LinkedList
from Node import Node

# Adding one node at a time to an empty LL.
print("-- Creating a LL one Element at a Time --")

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
print("-- Creating a LL with Initial Values--")

llist = LinkedList(["a", "b", "c", "d", "e"])
print(llist)

# Using the iterable in the LinkedList class.
print("-- Iterating through a LL --")

for node in llist:
    print(node)


# Adding a new node to the head of the LL
print("-- Adding a New Node to the Head of a LL --")

llist = LinkedList()
print(llist)

llist.add_first(Node("b"))
print(llist)

llist.add_first(Node("a"))
print(llist)


# Adding a new node to the end of the LL
print("-- Adding a New Node to the End of a LL --")

llist = LinkedList(["a", "b", "c", "d"])
print(llist)

llist.add_last(Node("e"))
print(llist)

llist.add_last(Node("f"))
print(llist)


# Adding a new node after an existing node in the LL
print("-- Adding a New Node after an Existing Node --")

#llist = LinkedList()
#llist.add_after("a", Node("b")) # Exception: List is empty.

llist = LinkedList(["a", "b", "c", "d"])
print(llist)

llist.add_after("c", Node("cc"))
print(llist)

#llist.add_after("f", Node("g")) # Exception: Node with data 'f' not found.


# Adding a new node before an existing node in the LL
print("-- Adding a New Node Before an Existing Node --")

llist = LinkedList(["b", "c"])
print(llist)

llist.add_before("b", Node("a"))
print(llist)

llist.add_before("b", Node("aa"))
llist.add_before("c", Node("bb"))
print(llist)


# Removing a node
print("-- Removing an Existing Node --")

llist = LinkedList(["a", "b", "c", "d", "e"])
print(llist)

llist.remove_node("a")
print(llist)

llist.remove_node("e")
print(llist)

llist.remove_node("c")
print(llist)
