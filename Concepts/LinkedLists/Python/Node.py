class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        """
        Provides a more helpful representation of the Node class.
        """
        return self.data
