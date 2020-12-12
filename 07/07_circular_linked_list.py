'''
07. Program to create a Circular singly linked list for 
    adding and deleting a Node.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class CircularLinkedList:
    def __init__(self):
        self.last = None
 
    # This function is only for empty list
    def AddElement(self, data):
 
        if (self.last != None):
            return self.last
 
        # Creating the newnode temp
        temp = Node(data)
        self.last = temp
 
        # Creating the link
        self.last.next = self.last
        return self.last
 
    def AddFront(self, data):
 
        if (self.last == None):
            return self.AddElement(data)
 
        temp = Node(data)
        temp.next = self.last.next
        self.last.next = temp
 
        return self.last
 
    def AddEnd(self, data):
 
        if (self.last == None):
            return self.AddElement(data)
 
        temp = Node(data)
        temp.next = self.last.next
        self.last.next = temp
        self.last = temp
 
        return self.last
 
    def AddAfter(self, data, item):
 
        if (self.last == None):
            return None
 
        temp = Node(data)
        p = self.last.next
        while p:
            if (p.data == item):
                temp.next = p.next
                p.next = temp
 
                if (p == self.last):
                    self.last = temp
                    return self.last
                else:
                    return self.last
            p = p.next
            if (p == self.last.next):
                print(item, "not present in the list")
                break
 
    def DisplayList(self):
        if (self.last == None):
            print("List is empty")
            return
 
        temp = self.last.next
        while temp:
            print(temp.data)
            temp = temp.next
            if temp == self.last.next:
                break

llist = CircularLinkedList()
last = llist.AddElement(6)
last = llist.AddFront(4)
last = llist.AddFront(2)
last = llist.AddEnd(8)
last = llist.AddEnd(12)
last = llist.AddAfter(10,8)
llist.DisplayList()