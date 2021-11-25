"""
Root -> first node
Edge ->  connection between the children 
Leaf -> the end child 
Parent -> 
Child -> 
"""


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
            return self
        current = self.root
        while True:
            if current.value == value:
                return None
            elif current.value < value:
                if current.left == None:
                    current.left == newNode
                    return self
                else:
                    current = current.left
            else:
                if current.right == None:
                    current.right = newNode
                else:
                    current = current.right

    def find(self, value):
        if self.root == None:
            return False
        current = self.root
        while current != None:
            if current.value == value:
                return current
            elif current.value < value:
                current = current.left
            else:
                current = current.right
        return None
