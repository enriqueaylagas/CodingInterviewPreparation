class Solution:
    def calPoints(self, operations: List[str]) -> int:

        recordStack = []
        
        for i in range(len(operations)): 
                
            if operations[i] == '+':
                recordStack.append(recordStack[-1] + recordStack[-2])
            elif operations[i] == 'D':
                recordStack.append(2*recordStack[-1])
            elif operations[i] == 'C':
                recordStack.pop()
            else:
                recordStack.append(int(operations[i]))
        

        return sum(recordStack)
        