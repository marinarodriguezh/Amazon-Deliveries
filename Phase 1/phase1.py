from doublylinkedlist import DoublyLinkedList
import random
import unittest
class Package:
    def __init__(self, ident, address, code):
        self.ident=ident
        self.address=address
        self.code=code
        self.tries=0

class Orders:
    def __init__(self):
        self.orders=DoublyLinkedList()
    
    def show(self):
        """Complexity O(n). The best case would be when the list is empty or it has 1 element.
        The worst case would be if there are too many nodes in the list."""
        result=''
        node=self.orders.head
        while node:
            result += str(node.element.ident)+ ' '
            node=node.next
        print(result[:-1])
        
class DSMember:
    def __init__(self, ident, name, surname, status, zone, packages):
        self.ident=ident
        self.name=name
        self.surname=surname
        self.status=status
        self.zone=zone
        self.packages=packages
        
    def show(self):
        """Complexity O(1). The best case would be when the list is empty or it has 1 element.
        The worst case would be if there are too many nodes in the list."""
        result=''
        result += str(self.ident)+ ' '
        result += str(self.status)+ ' '
        result += str(self.zone)+ ' '
        print(result[:-1], end=" ")
        self.packages.show()
        
class DSMembers:
    def __init__(self):
        self.members=DoublyLinkedList()
        self.sortedmembers=DoublyLinkedList()
    
    def sort(self):
        #sorts alphabetically the members
        """Complexity O(n^2). The best case would be when the list is empty or it has 1 element.
        The worst case would be if there are too many elements in the list and the last member in the list has the first surname."""
        memsort=self.members
        current = memsort.head;  
        index = None;  
        if(self.members.head == None):  
            return 
        else:  
            while(current != None):    
                index = current.next  
                while(index != None):  
                    #If current node's data is greater than index's node data, swap the data between them  
                    if(current.element.surname > index.element.surname):  
                        temp = current.element;  
                        current.element = index.element 
                        index.element = temp 
                    index = index.next 
                current = current.next  
        self.sortedmembers=memsort
   
    def deliverPackagesMemb(self, identifier):
        """Complexity O(n). The best case would be when the members do not have packages to deliver.
        The worst case would be if all members have many packages to deliver."""
        head=self.members.head
        while head.element.ident!=identifier:
             head=head.next
        member=head
        if member.element.packages.orders.isEmpty:
                    print("Packages processed")
        else:
                    package=member.element.packages.head
                    while package:
                        x=random.randint(1,2)
                        if x==1:
                            member.element.packages.removeFirst()
                            self.delivered.delivered.addLast(package.element)
                            print("Package: ", package.element.ident, " delivered ", "Tries: ", package.element.tries)
                            package=package.next
                        else:
                            member.element.packages.removeFirst()
                            member.element.packages.addLast(package.element)
                            print("Package: ", package.element.ident, " to be delivered after attempt number", package.element.tries)
                            package.element.tries+=1
                            if package.element.tries==3:
                                member.element.orders.removeLast()
                                self.incidents.incidents.addLast(package.element)
                                print("Package: ", package.element.ident, "removed")
                            package=package.next

    def showSorted(self):
        """Complexity O(n^3). The best case would be when the list is empty or it has 1 element.
        The worst case would be if there are too many elements in the list."""
        self.sort()
        node=self.sortedmembers.head
        while node:
            node.element.show()
            node=node.next
    
   
class Delivered:
    def __init__(self):
        self.delivered=DoublyLinkedList()

class Incidents:
    def __init__(self):
        self.incidents=DoublyLinkedList()

class AmazonManagement:
    def __init__(self, orders, members, delivered, incidents):
        self.orders=orders
        self.members=members
        self.delivered=delivered
        self.incidents=incidents
    
    def loadOrders(self, package):
        """Complexity O(1)"""
        self.orders.orders.addFirst(package)    
    
    def loadDSMembers(self, m):
        """Complexity O(1)"""
        self.members.members.addFirst(m)
    
    def showDSMembers(self):
        """Complexity O(n^3). The best case would be when the list of members is empty or it has 1 element.
        The worst case would be if there are too many elements in the list."""
        self.members.showSorted()
    
    def assignPackage(self, package):
            #goes through every element of the list looking for the member with the conditiones needed
            """Complexity O(n). The best case would be when the list is empty or if the member with the right conditions is the first element.
            The worst case would be if there is no member with the right conditions."""
            member=self.members.members.head
            while member:
                zone=member.element.zone.head
                while zone:
                    if member.element.status=="active" and package.code==zone.element:
                        member.element.packages.orders.addLast(package)
                        return True
                    zone=zone.next
                member=member.next
            return False

    def assignDefault(self, package):
            #if there isn't a member with the conditions needed, this function is used
            """Complexity O(n). The best case would be when the list is empty because it has to go through the whole list even if the member needed is the first element.
            The worst case would be if there are too many elements in the list."""
            previous = self.members.members.head.next
            current=self.members.members.head
            while previous:
                if current.element.zone.size > previous.element.zone.size:
                    current = previous
                current = current.next
            previous.element.orders.addLast(package)
            previous.element.zone.addLast(package.code)

    def assignDistribution2(self, package):
        #after getting the package this function is used 
        """Complexity O(n). The best case would be when the list is empty or the package is assigned to its member.
        The worst case would be if there are too many elements in the list and it could not find a member."""
        assigned = self.assignPackage(package)
        if not assigned:
           self.assignDefault(package)
        
    def assignDistribution(self):
        """Complexity O(n). The best case would be when the list is empty or the first members in the list have the conditions asked.
        The worst case would be if there isn't a member with the conditions after going through the whole list."""
        for a in range(self.orders.orders.size):
            package=self.orders.orders.getAt(a)
            self.assignDistribution2(package)

            
    def deliver(self):
        """Complexity O(n^2). The best case would be when the are not any members.
        The worst case would be if there are many members and they all have many packages to deliver."""
        head=self.members.members.head
        while head:
            self.members.deliverPackagesMemb(head.element.ident)
            head=head.next
            
    def removeDSMember(self, identifier):
        """Complexity O(n^3). The best case would be when the list of members is empty or it has 1 node.
        The worst case would be if after going through all the members, there is none with the conditions needed to get the package."""
        n=0
        head=self.members.members.head
        while head.element.ident!=identifier:
            head=head.next
            n+=1
        member=head
        if member.element.packages.orders.isEmpty==False:
            member.element.status="inactive"
            package=member.element.packages.head
            while package:
                a=self.members.members.head
                condition=True
                while a and condition:
                    b=self.members.members.zone.head
                    while b:
                        if a.element.status=="active" and package.element.code==b.element:
                            a.element.packages.addLast(package.element)
                            condition=False
                        else:
                            b=b.next
                a=a.next
                if condition==True:
                    self.incidents.incidents.addLast(package.element)
        self.members.members.removeAt(n)
                
class AmazonManagementTest(unittest.TestCase):
    
    pack=Package("132-1352234-332344","Avenida del Sur nº5", 28320)
    pack2=Package("132-1352234-332345","Alcachofa Street nº2", 28321)
    p=Orders()
    deliv=Delivered()
    incid=Incidents()
    zone1=DoublyLinkedList()
    zone1.addFirst(28321)
    zone2=DoublyLinkedList()
    zone2.addFirst(28320)
    m1=DSMember("R100222", "Laura","Segura", "active", zone1, p) 
    m2=DSMember("R100223", "Marina","Rodriguez", "inactive", zone2, p)
    m3=DSMember("R100224", "Pepe","Acosta", "inactive", zone1, p) 
    m4=DSMember("R1002225", "Rocio","Martinez", "active", zone2, p)
    m5=DSMember("R100226", "Diego","Garcia", "inactive", zone1, p)
    members=DSMembers()
    
    def setUP(self):
        self.am=AmazonManagement(p, members, delivp, incid)
        
    def loadOrderstest(self):
        self.am.loadOrders(pack)
    
    def loadMemberstest(self):
        self.am.loadDSMembers(m1)
        
    def showDSMemberstest(self):
        result=self.am.showDSMembers()
        assert result==m1
    
            
def test():
        
    pack=Package("132-1352234-332344","Avenida del Sur nº5", 28320)
    pack2=Package("132-1352234-332345","Alcachofa Street nº2", 28321)
    p=Orders()
    deliv=Delivered()
    incid=Incidents()
    zone1=DoublyLinkedList()
    zone1.addFirst(28321)
    zone2=DoublyLinkedList()
    zone2.addFirst(28320)
    m1=DSMember("R100222", "Laura","Segura", "active", zone1, p) 
    m2=DSMember("R100223", "Marina","Rodriguez", "inactive", zone2, p)
    m3=DSMember("R100224", "Pepe","Acosta", "inactive", zone1, p) 
    m4=DSMember("R1002225", "Rocio","Martinez", "active", zone2, p)
    m5=DSMember("R100226", "Diego","Garcia", "inactive", zone1, p)
    members=DSMembers()
    amazon=AmazonManagement(p ,members, deliv, incid)
    amazon.loadOrders(pack)
    amazon.loadOrders(pack2)
    amazon.loadDSMembers(m1)
    amazon.loadDSMembers(m2)
    amazon.loadDSMembers(m3)
    amazon.loadDSMembers(m4)
    amazon.loadDSMembers(m5)
    amazon.assignDistribution()
    amazon.deliver()
    amazon.removeDSMember("R100222")
    amazon.showDSMembers()

test()  

        
        
        
        
        
