# Question 155  - MinStack.

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

 

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2


class MinStack:

    def __init__(self):

        self.stack = [] # initialize list to act as the stack
        self.minStack = [] # initialize list to act as the stack that tracks the number with the least value
        

    def push(self, val: int) -> None:
        self.stack.append(val) # add value to the end of the stack
        val = min(val, self.minStack[-1] if self.minStack else val) # if minStack is not empty, then get the number with the least value between "val" and the last number in minStack and reassign it to "val" 
        self.minStack.append(val) # add that minimum number to the end of minStack
        
        

    def pop(self) -> None:
        self.stack.pop() # delete the last number in stack
        self.minStack.pop() # delete the last number in minStack
        

    def top(self) -> int:
        return self.stack[-1] # return the last number in stack
        

    def getMin(self) -> int:
        return self.minStack[-1] # return the last number in minStack, which would mean that you are getting the number with the list value currently in the stack


        
