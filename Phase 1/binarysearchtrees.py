from binarytrees import Node
from binarytrees import BinaryTree

class BinarySearchTree(BinaryTree):
    
    def insert(self,x):
        """inserts a new node, with element x, into the tree"""
        if self.root==None:
            self.root=Node(x)
        else:
            self.insertNode(self.root,x)
            
    def insertNode(self,node,x):
        """Inserts a new node (with the element x) inside of the subtree node"""
        if node.elem==x:
            # Duplicate elements are not allowed
            print(x,'already exists!!!')
            return
        
        if x<node.elem:
            if node.leftChild!=None:
                self.insertNode(node.leftChild,x)
            else:
                newNode=Node(x)
                node.leftChild=newNode
                newNode.parent=node
        else: #x>node.elem
            if node.rightChild!=None:
                self.insertNode(node.rightChild,x)
            else:
                newNode=Node(x)
                node.rightChild=newNode
                newNode.parent=node

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
 
    def find(self,x):
        """Returns the ndoe whose element is x. If it is not found, it returns None"""
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
        """Searches and removes the node whose element is x"""
        node=self.find(x)
        if node is None:
            print(x,' does not exist!!!')
            return
        print('removing ', x)
        self.removeNode(node)
        
    def removeNode(self,node):    
        """Auxiliary method to remove the node which takes as parameter"""
        #First case: no children
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
        
        #Second case: only one child
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
        
         #Second case: only one child
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
            
        #Third case: two children
        successor=node.rightChild
        while successor.leftChild is not None:
            successor=successor.leftChild
            
        #we replace the node's elem by the successor's elem
        node.elem=successor.elem
        #we remove the succesor from the tree
        self.removeNode(successor)
        
    def smallestElement(self):
        if self.root is None:
            print("The tree is empty")
        node=self.root
        while node.leftChild:
            node=node.leftChild
        return node.elem
    
    def biggestElement(self):
        if self.root is None:
            print("The tree is empty")
        node=self.root
        while node.rightChild:
            node=node.rightChild
        return node.elem
    def sumElems(self):
        return self.sumAll(self.root)
    def sumAll(self,node):
        if node is None:
            return 0
        return node.elem + self.All(node.leftChild) + self.sumAll(node.rightChild)

    def printTen(self):
        self.printTenn(self.root)
    def printTenn(self,node):
        if node is None:
           return
        if node.parent!=None and node.parent.parent!=None and node.parent.parent.elem%10==0:
            print(node.elem, end=' ')
        self.printTenn(node.leftChild)
        self.printTenn(node.rightChild)
        
    def predecessor(self,node):
        if node is None:
            return None
        if node.leftChild is None:
            print(node.elem, "The predecessor does not exist")
            return None
        predecessor=node.leftChild
        while predecessor.rightChild:
            predecessor=predecessor.rightChild
        return predecessor
    def successor(self,node):
        if node is None:
            return None
        if node.rightChild is None:
            print(node.elem, "The sucessor does not exist")
            return None
        successor=node.rightChild
        while successor.leftChild:
            successor=successor.leftChild
        return successor
    def removeNode2(self,node):    
        """Auxiliary method to remove the node which takes as parameter"""
        #First case: no children
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
        
        #Second case: only one child
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
        
         #Second case: only one child
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
            
        #Third case: two children
        predecessor=self.predecessor
        node.elem=predecessor.elem
        #we remove the succesor from the tree
        self.removeNode(predecessor)
        
