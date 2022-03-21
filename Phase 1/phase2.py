from binarysearchtrees import BinarySearchTree
from binarytrees import Node
from doublylinkedlist import DoublyLinkedList
from phase1 import DSMembers
from phase1 import DSMember
from phase1 import Package
from phase1 import Orders
class Zone:
    def __init__(self,zone):
        self.zone=zone
        self.distributors=DSMembers()
        
    def __gt__(self, zone):
        return self.zone> zone.zone

    def __lt__(self, zone):
        return self.zone < zone.zone

    def __ge__(self, zone):
        return self.zone >= zone.zone

    def __le__(self, zone):
        return self.zone <= zone.zone

    #def __eq__(self, zone):
     #   return self.zone == zone.zone

    def __ne__(self, zone):
        return self.zone != zone.zone

    def assignDistributor(self, distributor):
        """Complexity O(1)"""
        self.distributors.members.addFirst(distributor)
        
    def deleteDistributor(self,distributor):
        """Complexity O(n). The best case would be when the distributor is the first element in the list or when the list is empty. 
        The worst case would be if there are many distributors and it is the last one in the list."""
        a=self.distributors.members.contains(distributor)        
        self.distributors.members.removeAt(a)
    def showDistributors(self):
        """Complexity O(logn). The best case would be when there are not many distributors in the zone or it is empty. 
        The worst case would be when there are many distributors."""
        self.distributors.showSorted
        
class Zones:
    def __init__(self):
        self.zones=BinarySearchTree()
    def createZone(self,x):
        """Complexity O(logn). The best case would be when the tree already has a root. The worst case would be if the tree is empty"""
        self.zones.insert(x)
    def assignDistributor(self,zone,distributor):  
        """Complexity O(logn). The best case would be when the zone does not exist or it is the root.The worst case would be when the zone is the last node and there are too many nodes in the tree."""
        thezone=self.zones.find(zone)
        thezone.elem.assignDistributor(distributor)
    def deleteDistributor(self,zone,distributor):
        """Complexity O(logn). The best case would be when the zone does not exist or it is the root.The worst case would be when the zone is the last node and there are too many nodes in the tree."""
        thezone=self.zones.find(zone)
        thezone.elem.deleteDistributor(distributor)
    def showDistributors(self,zone):
        """Complexity O(logn). The best case would be when there are not many distributors in the zone or it is empty. The worst case would be when there are many distributors."""
        thezone=self.zones.find(zone)
        thezone.elem.showDistributors()
        
    def showZones(self):
        """Complexity O(logn). The best case would be when there are not many zones in the tree or it is empty. The worst case would be when there are many zones."""
        self._inorder2(self.zones.root)
        print()
    
    def _inorder2(self,currentNode):
        """Complexity O(logn). The best case would be when there are not many zones in the tree or it is empty. The worst case would be when there are many zones."""
        if currentNode!=None:
            self._inorder2(currentNode.leftChild)
            print(currentNode.elem.zone)
            currentNode.elem.showDistributors()
            self._inorder2(currentNode.rightChild) 
            
        
        
    def BalanSize(self, root):
        """Complexity O(logn). The best case would be when the tree is empty or there are not many nodes.The worst case would be if there are too many nodes in the tree and it would have to go through all of them."""
        if root is None:
            return
        ls = self.zones._size(root.leftChild) 
        rs = self.zones._size(root.rightChild)
        while abs(ls- rs) > 1:
            if ls>rs:
                #if self.zones.predecessor(root) is not None:
                pred=self.zones.predecessor(root)
                nod=Node(root.elem)
                if root.rightChild is not None:
                    self.zones.insertNode(root.rightChild,root.elem)
                else:
                    root.rightchild=nod
                root.elem=pred.elem
                self.zones.removeNode(pred)
            if ls<rs:
                #if self.zones.successor(root) is not None:
                suc=self.zones.successor(root)
                nod=Node(root.elem)
                if root.leftChild is not None:
                    self.zones.insertNode(root.leftChild,root.elem)
                else:
                    root.leftChild=nod
                root.elem=suc.elem
                self.zones.removeNode(suc)
            ls = self.zones._size(root.leftChild) 
            rs = self.zones._size(root.rightChild)
        self.BalanSize(root.leftChild)
        self.BalanSize(root.rightChild)
            

                
    def isBalancedSize(self, root): 
        """Complexity O(logn). The best case would be when the tree is empty or there are not many nodes.The worst case would be if there are too many nodes in the tree and it would have to go through all of them."""
        if root is None: 
            return True
        lh = self.zones._size(root.leftChild) 
        rh = self.zones._size(root.rightChild) 
        if (abs(lh - rh) <= 1) and self.isBalancedSize(root.leftChild) is True and self.isBalancedSize( root.rightChild) is True: 
            return True
        return False
    

    def isBalancedsize(self):
        """Complexity O(logn). The best case would be when the tree is empty or there are not many nodes.
        The worst case would be if there are too many nodes in the tree and it would have to go through all of them."""
        
        if self.isBalancedSize(self.zones.root)==True:
            return
        else:
            self.BalanSize(self.zones.root)
            
    def isBalancedHeight(self, root): 
        """Complexity O(logn). The best case would be when the tree is empty or there are not many nodes.
        The worst case would be if there are too many nodes and levels in the tree and it would have to go through all of them."""
        if root is None: 
            return True
        lh = self.zones._height(root.leftChild) 
        rh = self.zones._height(root.rightChild) 
        if (abs(lh - rh) <= 1) and self.isBalancedHeight(root.leftChild) is True and self.isBalancedHeight( root.rightChild) is True: 
            return True
        return False
   
    def rightRotation(self, node):  
       """Complexity O(1)"""
       child = node.leftChild
       grandchild = child.rightChild 
       child.rightChild = node
       node.leftChild = grandchild
       if grandchild!=None:
           grandchild.parent = node
       node.parent = child
  
       return child
            
    def leftRotation(self, node):   
       """Complexity O(1)"""
       child = node.rightChild
       grandchild = child.leftChild 
       child.leftChild = node
       node.rightChild = grandchild
       if grandchild!=None:
           grandchild.parent = node
       node.parent = child
  
       return child   
    
    def doubleLeftRotation(self,x):
        "Complexity O(logn)"
        x.rightChidl=self.rightRotation(x.rightChild)
        x=self.leftRotation(x)
        return x
        
    def doubleRightRotation(self,x):
        "Complexity O(logn)"
        x.leftChild=self.leftRotation(x.leftChild)
        x=self.rightRotation(x)
        return x
    
    def BalanHeight(self,root):
        """Complexity O(logn). The best case would be when the tree is empty or there are not many nodes.
        The worst case would be if there are too many nodes and levels in the tree and it would have to go through all of them."""
        if root is None:
            return
        if root.leftChild is not None:
            lh = self.zones._height(root.leftChild)
            if root.leftChild.leftChild is not None:
                llh = self.zones._height(root.leftChild.leftChild) 
            else:llh=0
            if root.leftChild.rightChild is not None:
                lrh = self.zones._height(root.leftChild.rightChild)
            else:
                lrh=0
        else:
            lh=0        
        if root.rightChild is not None:
            rh = self.zones._height(root.rightChild) 
            if root.rightChild.leftChild is not None:
                rlh = self.zones._height(root.rightChild.leftChild) 
            else:
                rlh=0
            if root.rightChild.rightChild is not None:
                rrh = self.zones._height(root.rightChild.rightChild)
            else:
                rrh=0
        else:
            rh=0
        if (rh-lh)>=1:
            if (rlh-rrh)>=1:
                root=self.doubleLeftRotation(root)
            else:
                root=self.leftRotation(root)
        if (lh-rh)>=1:
            if (lrh-llh)>=1:
                root=self.doubleRightRotation(root)
            else:
                root=self.rightRotation(root)
        return self.BalanHeight(root.leftChild), self.BalanHeight(root.rightChild)
    
    def isBalancedheight(self):
        """Complexity O(logn). The best case would be when the tree is empty or there are not many nodes.
        The worst case would be if there are too many nodes and levels in the tree and it would have to go through all of them."""
        if self.isBalancedHeight(self.zones.root)==True:
            return
        else:
            self.BalanHeight(self.zones.root)



    def distribute(self, currentNode, l):
        """Complexity O(logn). The best case would be when the zone does not have many distributors.
        The worst case would be when the zone has many distributors and it would have to go through the tree until they are all reasssigned."""
        if currentNode != None:
            nodeDistributors = currentNode.elem.distributors
            distribut = l.getAt(0) 
            l.removeAt(0)
            nodeDistributors.addLast(distribut)
            return self.distribute(currentNode.leftChild, l), self.distribute(currentNode.rightChild, l)
    

    def deleteZone(self, zone):
        """Complexity O(logn). The best case would be when the zone does not have many distributors.
        The worst case would be when the zone has many distributors and it would have to go through the tree until they are all reasssigned."""
        node = self.find(zone)
        members = node.elem.distributors

        upperList = DoublyLinkedList()
        lowerList = DoublyLinkedList()

        if members.size == 0:
            self.removeNode(node)

        else:
            size = members.size % 2

            #List for parents
            for i in range(0, size):
                element = members.getAt(i)
                upperList.addLast(element)

            #List for children 
            for i in range(size, members.tail):
                element = members.getAt(i)
                lowerList.addLast(element)

            #Distribution for children
            size = lowerList.size
            while size > 0:
                self.distributed(node, lowerList)

            #Distribution for parents 
            size = upperList.size
            while size > 0:
                parent = node.parent
                if parent == None:
                    node = self.find(zone)
                else:
                    for i in range(upperList):
                        element = upperList.getAt(i)
                        parent.element.distributors.addLast(element)
                        upperList.removeAt(i)
                        node = parent
       
def test():
    tree=Zones()
    for i in range(5):
        tree.createZone(Zone(i))
    pack=Package(33,"Avenida del Sur", 28320)
    pack2=Package(44,"Calle Alcachofa", 28321)
    p=Orders()
    zone1=DoublyLinkedList()
    zone1.addFirst(28321)
    zone2=DoublyLinkedList()
    zone2.addFirst(28320)
    m1=DSMember("R100222", "Laura","Segura", "active", zone1, p) 
    m2=DSMember("R100223", "Marina","Rodriguez", "inactive", zone2, p)
    m3=DSMember("R100224", "Pepe","Acosta", "inactive", zone1, p) 
    m4=DSMember("R1002225", "Rocio","Martinez", "active", zone2, p)
    m5=DSMember("R100226", "Diego","Garcia", "inactive", zone1, p)
    tree.showZones()
    tree.assignDistributor(Zone(0),m1)
    tree.assignDistributor(Zone(2),m2)
    tree.assignDistributor(Zone(3),m3)
    tree.assignDistributor(Zone(4),m4)
    tree.assignDistributor(Zone(1),m5)
    tree.showDistributors(zone1)
    tree.showDistributors(zone2)
    tree.deleteZone(zone1)
    tree.showDistributors(zone1)
    #tree.isBalancedheight()
   # x=tree.isBalancedHeight(tree.zones.root)
    #if x==True:
    #   print("si")
    #else:
    #    print("no")
    
test()
