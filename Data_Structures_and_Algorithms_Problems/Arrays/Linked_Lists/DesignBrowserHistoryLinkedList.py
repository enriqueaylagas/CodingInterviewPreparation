# Question 1472. Design Browser History (Linked List Solution)

# You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

# Implement the BrowserHistory class:

# BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
# void visit(string url) Visits url from the current page. It clears up all the forward history.
# string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
# string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
 

# Example:

# Input:
# ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
# [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
# Output:
# [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]


class Url: # class to create new URLs (nodes)
    def __init__(self,url: str):
        self.url = url # same as val in a regular node class
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Url(homepage) # initializing a current pointer to keep track of the URL we are at
    
    def visit(self, url: str) -> None:
        newUrl = Url(url)       # creating a new URL node
        self.current.next = newUrl # setting the next node to be the new URL
        newUrl.prev = self.current # setting the new node to be pointing to the previous node as-well
        
        self.current = newUrl # setting the current node to be in the newUrl (updating where we are in the linked list)

    def back(self, steps: int) -> str:

        while self.current.prev and steps > 0: # checking if a previous URL exists and if the steps are greater than 0, to go back in the linked list
            self.current = self.current.prev # going back one step to the previous node
            steps -=1 # decreasing the steps to break out of the loop once steps reaches 0 or current.prev is Null

        
        return self.current.url # return the URL after doing so

    def forward(self, steps: int) -> str:

        while self.current.next and steps > 0:  # checking if a next URL exists and if the steps are greater than 0, to go back in the linked list
            self.current = self.current.next # going forward in the lest one node
            steps -=1 # decreasing the steps to break out of the loop once steps reaches 0 or current.prev is Null

        return self.current.url # return the current URL after doing so


