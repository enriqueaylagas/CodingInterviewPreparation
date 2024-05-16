# Question 20.

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 



class Solution:
    def isValid(self, s: str) -> bool:

        stack = [] # stack/list to pop the last symbol if it matches to the correct symbol
        parenMap = {")":"(", "]":"[", "}":"{"} #  dictionary to map each closing parenthesis symbol to the respective opening 


        for parenSymbol in s:

            if parenSymbol in parenMap: # if parenSymbol is a closing symbol, then this will pass

                if stack and stack[-1] == parenMap[parenSymbol]: # if stack is not empty and the last symbol in the stack matches parenSymbol's counterpart, this will pass

                    stack.pop() # if so, pop(delete) that last symbol because we know it is valid

                else:
                    return False # if it isn't, we already know it isn't valid, therefore, the whole string isn't valid

            else: # if parenSymbol is an opening symbol, this will pass

                stack.append(parenSymbol) #if so, we must add that opening symbol to the stack

        return True if not stack else False # if stack is empty return True (because we would have popped all valid parenthesis). if it isn't empty, we know there was at least one unvalid parenthesis, therefore, we return False