class Node:
    def __init__(self, value):
        
        self.node = None
    
    def flip_node(self): 
        raise NotImplementedError("Error: Method Not Implemented")
    
    def __str__(self):
        raise NotImplementedError("Error: Method Not Implemented")
    
class Leaf(Node):
    def __init__(self, node:str):
        self.node = str(node)
        
    def flip_node(self):
        return self.node
    
    def __str__(self):
        return  f"{self.node} "

class Internal(Node):
    def __init__(self, node: str, left: Node, right: Node):
        self.node = node
        self.left = left
        self.right = right
        
    def flip_node(self): 
        right = self.right
        left = self.left
        self.left = right
        self.right = left
        return self.left.flip_node(), self.right.flip_node()
       
    def __str__(self):
        return f"<{self.node}, {self.left}, {self.right}>"
    

def main():  
    l1 = Leaf(3) 
    l2 = Leaf(6) 
    l3 = Leaf(9) 
    i = Internal(7, l2, l3) 
    tree = (Internal(5, l1, i))
    print (f"Original Tree: {tree}")
    tree.flip_node()
    print(f"Flipped Tree: {tree}")
    
    
    d = Leaf("d") 
    e = Leaf("e") 
    f = Leaf("f") 
    n = Leaf("None")
    b = Internal("b", d, e) 
    c = Internal("c", f, n)
    
    treeA = Internal("a", b, c)
    print (f"Original Tree: {treeA}")
    treeA.flip_node()
    print(f"Flipped Tree: {treeA}") 
if __name__ == '__main__': 
    main()
     