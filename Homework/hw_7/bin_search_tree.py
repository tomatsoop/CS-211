"""
CS 211 - HW 7
Sabrina Zhang 
Binary Search Tree - Implement Method find_min() find_max()
"""


class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
        else:
            self.root.insert(new_node)
    
    def __str__(self):
        return f"T({self.root})"
    
    def search(self, val):
        if self.root == None:
            return None
        else:
            return self.root.search(val)
        
    def find_min(self):
        """
        Finds the minimum value in the binary search tree.
        Returns:
            The node with the minimum value.
        """
        return self.root.find_min()
        
    def find_max(self):
        """
        Finds the maximum value in the binary search tree.
        Returns:
            The node with the maximum value.
        """
        return self.root.find_max()
    
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def __str__(self):
        # return f"({self.data} {(self.left) if self.left else '.'} {(self.right) if self.right else '.'})"
        return f"({self.data} {self.left} {self.right})"
    
    def insert(self, node):
        if self.data != node.data:
            if node.data < self.data:
                if self.left == None:
                    self.left = node
                else:
                    self.left.insert(node)
            elif self.right == None:
                self.right = node
            else:
                self.right.insert(node)
        return
   
    
    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return None
        if self.right:
            return self.right.search(val)
        else:
            return False

    def find_min(self):
        """
        Recursively finds the minimum value in the subtree rooted at the current node.
        Returns:
            The node with the minimum value.
        """
        
        if self.left == None:
            return self.data
        if self.left.data < self.data:
            return self.left.find_min()
        
    def find_max(self):
        """
        Recursively finds the maximum value in the subtree rooted at the current node.
        Returns:
            The node with the maximum value.
        """
        if self.right == None:
            return self.data
        if self.right.data > self.data:
            return self.right.find_min()
        
if __name__ == "__main__":
    t = Tree()
    [t.insert(value) for value in [30, 10, 5, 40, 7]]
    print(t)

    print(t.search(10))
    print(t.search(11))
    print(f"Finding Min: {t.find_min()}")
    print(f"Finding Max: {t.find_max()}")

