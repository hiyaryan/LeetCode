# Linked Lists (in Python)
Linked lists (LL) are an ordered collection of objects.
Differs from lists by how they are stored in memory. Lists are stored contiguously, LL are not.

## Concepts
Elements are stored as *nodes*.
Every node has two fields:
1. Data: contains the value to be stored in the node.
2. Next: contains a reference to the next node.
3. Head: the first node in the LL
4. Tail: the last node in the LL

## Applications
LL are used to implement queues, stacks, and graphs.
They are also used to manage lifecycle management for an OS application.

### Queues
FIFO "First-in First-out"
The first element that goes into the list is the first element to be retrieved.

### Stacks
LIFO "Last-in First-out"
The last elemet that goes into the list is the first element to be retrieved.

### Graphs
Show *relationships* between objects or represents different types of *networks*.
**Adjacency list** a list of LL where each vertex of the graph is stored alongside a collection of connected variables.

## Performance
Lists and LL are are not so different in terms of memory usage since Lists re dynamic arrays.
They do differ in terms of time:
1. Insertion and Deletion
Lists
O(1) for insertion toward the end of the list
O(n) for insertion toward the beginning of the list

LL
O(1) for insertion at the beginning of a list *best for the queue data structure*
O(n) for insertion at the end of a list *same as lists for stack data structure*

2. Retrieval
Lists
O(1) when the index is known

LL 
O(n) even when the index is known it must traverse all elements to access the element

## `collections.deque`
deque (prnounced "deck") stands for *double-ended queue*.
Allows for the access, insertion, and removal of elements from the beginning or end of a list.

## Implementation of Queues and Stacks
Main difference in Queues and Stacks is how elements are retrieved.

### Queues (FIFO)
E.g. add people to a seating list at a restaurant based on when they arrived.
Add values to a list (enqueue), then remove the value thats been on the list the longest (dequeue).
deque *common queue functions*: `append` and `popleft`

### Stacks (LIFO)
E.g. a browsers history functionality that allows a user to go back from the last resource in the history.
The last element that is inserted on the stack should be the first to be removed.
deque *common stack functions*: `appendleft` and `popleft`


## Creating a Linked List Data Structure
Creating an LL from scratch is great for:
1. Practicing Python.
2. Learning about data structure theory.
3. Preparing for job interviews.

### Steps
Create a class to represent the LL containing
1. The **head** of the list.
Note: see LinkedList.py

Create a class to represent a Node in the LL. containing
1. The **value** of the node.
2. The **next** node.
Note: see Node.py

### Traversing a LL
How to go through every single node starting with the head of the LL and ending at None.

Using the __iter__ magic method, yield the result of each node while node is not None.
Note: see LinkedList.py

### Inserting a New Node
**Inserting at the beginning**
1. Create a new node.
2. Reference the next node in the new node as this head.
3. Point the new node to the head of the list.

Note: see LinkedList.py

**Inserting at the end**
1. Create a new node
2. Traverse the LL to the last node

Inserting a node at the end of the LL is required since it cannot be determined which node is last in the list.

Note: see LinkedList.py

**Inserting Between Two Notes**
Two approached:
I. Inserting *after* an existing node
1. Traverse the LL for some identifiable data.
2. If found set the next node of the new node to the next node of the current node.
3. Then set the next node of the current node to the new node.

II. Inserting *before* and existing node
1. Traverse the LL for some identifiable data.
2. Keep a reference variable of the previous node.
2. If found set the next node of the new node to the next node of the previous node.
3. Then set the next node of the current node to the new node.

Note: see LinkedList.py

**Removing a Node**
1. Traverse the LL for some identifiable data.
2. Link the previous node with the next node of the current node.

Note: see LinkedList.py
