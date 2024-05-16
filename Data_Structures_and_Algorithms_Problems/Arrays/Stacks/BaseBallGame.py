# Question 682 Basball Game.

# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.

# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.




# Example 1:

# Input: ops = ["5","2","C","D","+"]
# Output: 30
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.



class Solution:
    def calPoints(self, operations: List[str]) -> int:

        recordStack = []
        
        for i in range(len(operations)): 
                
            if operations[i] == '+': # if i is the plus sign, add the sum of the last two numbers in the ""operations list" into "recordStack"
                recordStack.append(recordStack[-1] + recordStack[-2])
            elif operations[i] == 'D': # if i is "D", add the last number in the ""operations list" times 2 into "recordStack""
                recordStack.append(2*recordStack[-1])
            elif operations[i] == 'C': # if i is "C", remove the last number in recordStack
                recordStack.pop()
            else:  # if the stack is any number, converted into an integer and add it to "recordStack"
                recordStack.append(int(operations[i]))
        

        return sum(recordStack) # add all the numbers in "recordStack" and return it 
        