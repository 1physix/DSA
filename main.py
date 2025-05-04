#Singly-Linked Lists

class SingleNode: #initiate Node class

    def __init__(self, val, next = None): #each node in a singly-linked list has 2 properties - it's value, and the value it points to, which is set to None by default
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)

head1 = SingleNode(1) #setting up the head node and following nodes.
A1 = SingleNode(3)
B1 = SingleNode(5)
C1 = SingleNode(7)

head1.next = A1 # how to actually link the lists
A1.next = B1
B1.next = C1

def display1(head): # making a way to display the list in a nice fashion.
    elements = []
    """How to traverse a singly linked list"""
    curr = head
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    """End of traversal"""
    print(" -> ".join(elements))

#display1(head)


#Doubly-Linked Lists
"A doubly-linked list has 3 main characteristics: the current value, the next value it points to, and the previous value it also points to."

class DoubleNode: #initiate Node class

    def __init__(self, val, next = None, prev = None): 
        self.val = val
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.val)

head2 = DoubleNode(1)
A2 = DoubleNode(4)
B2 = DoubleNode(9)
C2 = DoubleNode(16)

head2.next = A2
A2.next = B2
B2.next = C2

"""This is different to the Single-Linked List. Notice how each node is linked to the previous one AS WELL as the next one? This is why DLL is more useful in real situations."""
A2.prev = head2
B2.prev = A2
C2.prev = B2

curr = head2

def display2(head): #same display function, traversal is the same
    elements = []
    curr = head
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" <-> ".join(elements))

display2(head2)