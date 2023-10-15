#----------------------------------------------------
# Stack implementation #2 
# (Top of stack corresponds to back of list)
# 
# Author: CMPUT 175 team
# Updated by: Harmanpreet Singh Phull
#----------------------------------------------------

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    # MODIFY: RAISE AN EXCEPTION IF THIS METHOD IS INVOKED ON AN EMPTY STACK
    def pop(self):
        if (self.size() > 0):
            return self.items.pop()
        else:
            raise Exception

    # MODIFY: RAISE AN EXCEPTION IF THIS METHOD IS INVOKED ON AN EMPTY STACK
    def peek(self):
        if (self.size() > 0):
            return self.items[len(self.items)-1]
        else:
            raise Exception
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def show(self):
        print(self.items)
    
    def __str__(self):
        stackAsString = ''
        for item in self.items:
            stackAsString += item + ' '
        return stackAsString
    
    def clear(self):
        self.items.clear()