# Question 206. Reverse Linked ListNode

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


    	current = head # create a pointer value which points to head
    	prev = None # create a None value which will act as our pointer to the previous Node


    	while current: # while current isn't None this will pass

    		nxt = current.next # create a "nxt" variable to keep the pointer to the next node on the list
    		current.next = prev # set the next point to our previous Node
    		prev = current	# set ahora previous pointer to ahor current Node
    		current = nxt # set current Node to the next on the list to go on


    		#once we are done re-setting all of our pointers to the previous ones on the list


    	return prev # we return our previous pointer since it contains the information about all of the linked list (now in reverse)


    	
    	Example

    	p = prev
    	c = current
    	cn = current.next
    	
    
                     
      		p     c  cn
    	0 - None [1] -> [2] -> [3] -> [4] -> [5]-> None

    		nxt =  ->[2]
    		current.next = None<-
    		prev = [1]->
    		current = [2]
    				         cn	 p      c  
    		which means None <- [1] -> [2] -> [3] -> [4] -> [5]

 #		---------------------------------------------------------   	
    	
    	 	     cn  p      c  
    	1.	None <- [1] -> [2] -> [3] -> [4] -> [5]

    		nxt = ->[3]
    		current.next = [1]<-
    		prev = [2]->
    		current = [3]

    		                         cn  p      c  
    		 which means None <- [1] <- [2] -> [3] -> [4] -> [5]

#		---------------------------------------------------------
    				    cn  p      c  
    	2.	None <- [1] <- [2] -> [3] -> [4] -> [5]

    		nxt = ->[4]
    		current.next = [2]<-
    		prev = [3]->
    		current = [4]

    		                               cn  p      c  
    		which means None <- [1] <- [2] <- [3] -> [4] -> [5]

#		---------------------------------------------------------
    					       cn  p      c  
    	3.	None <- [1] <- [2] <- [3] -> [4] -> [5]

    		nxt = ->[5]
    		current.next = [2]<-
    		prev = [4]->
    		current = [5]

    		                                      cn  p      c  
    		which means None <- [1] <- [2] <- [3] <- [4] -> [5] -> None

#		---------------------------------------------------------
    					              cn  p      c  
    	4.	None <- [1] <- [2] <- [3] -> [4] -> [5]

    		nxt = ->[5]
    		current.next = [2]<-
    		prev = [4]->
    		current = [5]

    		                                             cn  p    c  
    		which means None <- [1] <- [2] <- [3] <- [4] <- [5]   None

#		---------------------------------------------------------

    		# time complexity would be O(n) and space complexity would be O(1) 
    		# since we are passing through the LinkedList only once and we don't allocate any extra memory


#		-------------------------------------------------------------------------------------------------------------------

# RECURSIVE SOLUTION

class RecursiveSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


  		if not head:
  			return None

  		newHead = head

  		if head.next:
  			newHead = self.reverseList(head.next)
  			head.next.next = head

  		head.next = None
  		return newHead



  





















