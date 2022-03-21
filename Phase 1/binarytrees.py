class Node:
    def __init__(self,elem=None):
        self.elem=elem
        self.leftChild=None
        self.rightChild=None
        self.parent=None

class BinaryTree:
    def __init__(self):
        self.root=None
    
    def size(self,currentNode):
        if currentNode==None:
            return 0
        return 1+self.size(currentNode.leftChild)+self.size(currentNode.rightChild)
    
    def height(self,currentNode):
        if currentNode==None:
            return -1
        return 1+max(self.height(currentNode.leftChild),self.height(currentNode.rightChild))
    
    def depth(self, currentNode):
        if currentNode==None:
            return 0
        return 1+self.depth(currentNode.parent)
    
    def preorder(self,currentNode):
        if currentNode!=None:
            print(currentNode.elem,end=" ")
            self.preorder(currentNode.leftChild)
            self.preorder(currentNode.rightChild)
            
    def inorder(self,currentNode):
        if currentNode!=None:
            self.inorder(currentNode.leftChild)
            print(currentNode.elem,end=" ")
            self.inorder(currentNode.rightChild)
            
    def levelorder(self):
        if self.root==None:
            print("tree is empty")
            return
        print("level-order traversal")
        q=queue.Queue()
        q.enqueue(self.root)
        
        while q.empty()==False:
            current=q.dequeue()#dequeue
            print(current.elem, end=" ")
            if current.leftChild:
                q.enqueue(current.leftChild)
            if current.rightChild:
                q.enqueue(current.rightChild)
        print()
        
    def search(self,x):
            return self.searchNode(self.root,x)
            
    def searchNode(self,node,x):
            """Auxiliary method to search a node with value x"""
            if node is None:
                return False
            if node.elem==x:
                return True
            if x<node.elem:
                return self.searchNode(node.leftChild,x)
            if x>node.elem:
                return self.searchNode(node.rightChild,x)
        
    def insert(self,x):
            """inserts a new node, with element x, into the tree"""
            if self.root==None:
                self.root=Node(x)
            else:
                self.insertNode(self.root,x)
                
    def insertNode(self,node,x):
            if node.elem==x:
                print(x,"already exists!!!")
                return
            if x<node.elem:
                if node.leftChild!=None:
                    self.insertNode(node.leftChild,x)
                else:
                    newNode=Node(x)
                    node.leftChild=newNode
                    newNode.elem
            else: #x>node.elem
                if node.rightChild!=None:
                    self.insertNode(node.rightChild,x)
                else:
                    newNode=Node(x)
                    node.rightChild=newNode
                    newNode.parent=node
                    
    def find(self,x):
            return self.findNode(self.root,x)
        
    def findNode(self,node,x):
            if node is None:
                return None
            if node.elem==x:
                return node
            if x<node.elem:
                return self.findNode(node.leftChild,x)
            if x>node.elem:
                return self.findNode(node.rightChild,x)
        
    def remove(self,x):
            """searches and removes the node whose element is x"""
            node=self.find(x)
            if node is None:
                print(x,"does not exist!!!")
                return
            print("removing",x)
            self.removeNode(node)
            
    def removeNode(self,node):
            """Auxiliary method to remove the node which takes as parameter"""
            if node.leftChild is None and node.rightChild is None:
                parent_node=node.parent
                if parent_node is not None:
                    if parent_node.leftChild==node:
                        parent_node.leftChild=None
                    else:
                        parent_node.rightChild=None
                    node.parent=None
                else:
                    self.root=None
                return
            
            if node.leftChild is not None and node.rightChild is None:
                parent_node=node.parent
                if parent_node is not None:
                    if parent_node.leftChild==node:
                        parent_node.leftChild=node.leftChild
                    else:
                        parent_node.rightChild=node.leftChild
                    node.leftChild.parent=parent_node
                else:
                    self.root=node.leftChild
                return
            
            if node.leftChild is None and node.rightChild is not None:
                parent_node=node.parent
                if parent_node is not None:
                    if parent_node.leftChild==node:
                        parent_node.leftChild=node.rightChild
                    else:
                        parent_node.rightChild=node.rightChild
                    node.rightChild.parent=parent_node
                else:
                    self.root=node.rightChild
                return
            
            
        
###### ejercicios lab class #####
        
    def smallest(self):
        left=self.root.leftChild
        while left!=None:
            left=left.leftChild
        return left
    
    def maximum(self):
        right=self.root.rightChild
        while right!=None:
            right=right.rightChild
        return right
    
    def sumAll(self, root):
        if root.leftChild!=None:
            if root.rightChild!=None:
                return root.elem+self.sumAll(root.leftChild)+self.sumAll(root.rightChild)
            else: 
                return root.elem+self.sumAll(root.leftChild)
        else:
            if root.rightChild!=None:
                return root.elem+self.sumAll(root.rightChild)
            else:
                return root.elem
    
    #def grandparents(self, root):
        
    def predecessor(self, root):
        while root.leftChild!=None:
            root=root.rightChild
        return root.parent
        
    def successor(self, root):
        while root.rightChild!=None:
            root=root.leftChild
        return root.parent
        
    