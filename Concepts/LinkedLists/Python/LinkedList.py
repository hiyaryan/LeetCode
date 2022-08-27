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


    def add_first(self, node):
        """
        Add a node to the beginning of the list.
        """
        node.next = self.head
        self.head = node
    
    
    def add_last(self, node):
        """
        Add a node to the end of the list.
        """
    
        if self.head is None:
            self.head = node
            return
            
        for current_node in self:
            pass
                
        current_node.next = node


    def add_after(self, target_node_data, new_node):
        """
        Add a node after an existing node.
        """
    
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f"Node with {target_node_data} not found")


    def add_before(self, target_node_data, new_node):
        """
        Add a node before an existing node.
        """

        if self.head is None:
            raise Exception("List is empty")
    
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                new_node.next = prev_node.next
                prev_node.next = new_node
                return

            prev_node = node

        raise Exception(f"Node with {target_node_data} not found")

        
    def remove_node(self, target_node_data):
        """
        Remove a node.
        """

        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
        
            prev_node = node
    
        raise Exception(f"Node with {target_node_data} not found")
        
        
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
