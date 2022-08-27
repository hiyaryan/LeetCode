from Node import Node

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
    
        # Allows the quick creation of a linked list with some data
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        """
        Provides a more helpful representation of the LinkedList class.
        """
        
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next

        nodes.append("None")
        
        return " -> ".join(nodes)

    def __iter__(self):
        """
        Iterable for the LinkedList class that yields every single node.
        """
        node = self.head
        
        while node is not None:
            yield node
            node = node.next
