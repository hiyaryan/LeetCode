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
