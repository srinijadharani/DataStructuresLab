'''5a. 
Write a program to create a singly linked list for the following operations
• Insert a Node at Beginning, at Ending and at a given Position
• Delete a Node at Beginning, at Ending and at a given Position
• Search, Count the Number of Nodes and Display'''

class Node:
    # create a node for the linked list
    def __init__(self, data=None):
        self.data = data
        self.next = None

# create a singly linked list class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # insert an element at the beginning
    def AddFirst(self,newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode
    # insert an element at the end
    def AddLast(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        last_element = self.head
        while(last_element.next):
            last_element = last_element.next
        last_element.next=NewNode
    # insert an element in the middle of the linked list
    def AddBetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode
    # remove a specified element
    def RemoveElement(self, remove_key):
        head = self.head
        if (head is not None):
            if (head.data == remove_key):
                self.head = head.next
                head = None
                return

        while (head is not None):
            if head.data == remove_key:
                break
            prev = head
            head = head.next
        print("Removed Element is", remove_key)
        if (head == None):
            return
        prev.next = head.next
        head = None
    # display the linked list
    def DisplayList(self):
        print_element = self.head
        while print_element is not None:
            print (print_element.data)
            print_element = print_element.next
    # count the number of nodes
    def CountNodes(self, node):
        count = 0
        while node:
            count +=1
            node=node.next
        return count
    # search for an element
    def SearchElement(self, search_element):
        current_node = self.head
        while current_node != None:
            if current_node.data == search_element:
                print("Element {} found." .format(search_element))
            current_node = current_node.next

# create an instance of the class SinglyLinkedList
sll = SinglyLinkedList()
sll.head = Node(10)
e2 = Node(20)
e3 = Node(30)
sll.head.next = e2
e2.next = e3
sll.AddFirst(0)
sll.AddLast(50)
sll.AddBetween(sll.head.next, 40)
sll.DisplayList()
sll.RemoveElement(30)
sll.SearchElement(40)
