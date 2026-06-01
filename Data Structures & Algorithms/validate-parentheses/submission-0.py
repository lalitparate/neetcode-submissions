class Solution:
    def isValid(self, s: str) -> bool:
        
        myStack = []

        myDict = {')': "(", "}": "{", "]": "["}

        for c in s:
            if not myStack:
                myStack.append(c)
            else:
                if c in myDict and myStack[-1] == myDict[c]:
                    myStack.pop(-1)
                else:
                    myStack.append(c)
        print(myStack)
        return True if not myStack else False