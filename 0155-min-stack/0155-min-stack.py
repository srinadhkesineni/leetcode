class MinStack:

    def __init__(self):
        stack=[]
        self.s=stack
        self.min_stack=[]
        

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.min_stack or val<=self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.s[-1]==self.min_stack[-1]:
            self.min_stack.pop()
        return self.s.pop()
        
        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()