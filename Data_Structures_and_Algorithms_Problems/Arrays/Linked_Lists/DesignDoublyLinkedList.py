# Question 707. Design Linked List


# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

# Implement the MyLinkedList class:

# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the linked list.
# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

# Example 1:

# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]

# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3




class ListNode: # ListNode class for individual node creation
    def __init__(self,val):
        self.val  = val         # value of node
        self.next = None        # next node pointer
        self.prev = None        # previous node pointer

class MyLinkedList: # class to link the nodes together and do operations on it (when initialized this class will start out with two dummy nodes (left and right))

    def __init__(self):
        self.left = ListNode(0)             # dummy left node
        self.right = ListNode(0)            # dummy right node
        self.left.next = self.right         # next pointer for left dummy
        self.right.prev = self.left         # previous pointer for right dummy
       

    def get(self, index: int) -> int:

        current  = self.left.next               # setting current to the next pointer of left (first real node if it exists)
        

        while current and index > 0:            # checking if current node exists and if index is greater than 0
            current = current.next              # going to next pointer
            index -= 1                          # decreasing index variable for it to break out when it gets to 0 
         
        if current and current != self.right and index == 0:            # checking if current isn't null, if current isn't pointing to right dummy node, and if index is 0 (checking if we are in the correct node)
            return current.val                                          # returning the value of the index that was asked in the parameter passed

        return -1                                                       # return -1 if this fails (out of bounds)
     

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)         # creating new node with the value set in the parameter passed
        nxt = self.left.next            # setting a pointer to the next node so we don't lose it

        self.left.next = newNode            # re-setting left next pointer to point to the new node
        nxt.prev = newNode                  # re-setting the previous pointer of the next node to the new node
        newNode.next = nxt                  # setting the next pointer of the new node to the node the was at the head before
        newNode.prev = self.left            # setting the previous pointer of the new node to the dummy left node

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)             # creating new node with the value set in the parameter passed
        previous = self.right.prev          # setting a pointer to the previous node so we don't lose it


        previous.next = newNode             # setting the next pointer of the previous node to the new node
        self.right.prev = newNode           # setting the previous pointer of the right dummy node to the new node
        
        newNode.next = self.right           # setting the next pointer of the new node to the right dummy node
        newNode.prev = previous             # setting the previous pointer of the new node to the node that was previously at the tail
       

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = ListNode(val)             # creating new node with the value set in the parameter passed

        current = self.left.next            # setting current to the next pointer of left (first real node if it exists)

        while current and index > 0:        # checking if current node exists and if index is greater than 0
            current = current.next          # going to next pointer
            index -=1                       # decreasing index variable for it to break out when it gets to 0

        if current and index ==0:           # checking if the current node isn't null and if the index isn't 0
            

            newNode.next = current          # setting the next pointer of the new node to the current node
            newNode.prev = current.prev     # setting the previous pointer of the new node to the previous node

            current.prev.next= newNode      # setting the next pointer of the previous node to the new node
            current.prev = newNode          # setting the previous pointer of the current node to the new node


    def deleteAtIndex(self, index: int) -> None:

        current = self.left.next            # setting current to the next pointer of left (first real node if it exists)


        while current and index >0:         # checking if current node exists and if index is greater than 0

            current = current.next          # going to next pointer
            index -=1                       # decreasing index variable for it to break out when it gets to 0

        if current and current != self.right and index ==0:             # checking if current isn't null, if current isn't pointing to right dummy node, and if index is 0 (checking if we are in the correct node)
            current.next.prev = current.prev                            # setting the previous pointer of the next node to the previous node 
            current.prev.next = current.next                            # setting the next pointer of the previous node to the next node



# Example in practice


# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]



1. "MyLinkedList":  (initialize the linked list) -> current linked list: (left)[0]-><-[0](right)
2. "addAtHead" - [1]: (add the value 1 to the head of the linked list) -> current linked list: (left)[0]-><-[1]-><-[0](right)
3. "addAtTail" - [3]: (add the value 3 to the head of the linked list) -> current linked list: (left)[0]-><-[1]-><-[3]-><-[0](right)
4. "addAtIndex" - [1,2]: (add the value 2 to index 1 of the linked list) -> current linked list: (left)[0]-><-[1]->[2]<-[3]-><-[0](right)
5. "get" - [1]: (get the value of the node at index 1 of the linked list) -> current linked list: (left)[0]-><-[1]->[2]<-[3]-><-[0](right) -> the value 2 is at index 1
6. "deleteAtIndex" - [1] (delete the node at index 1 of the linked list) -> current linked list: (left)[0]-><-[1]-><-[3]-><-[0](right)
7. "get" - [1]: (get the value of the node at index 1 of the linked list) -> current linked list: (left)[0]-><-[1]-><-[3]-><-[0](right) -> the value 3 is now at index 1 after deleting the node with value 2 


