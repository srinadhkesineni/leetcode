class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        stack = []
        
        while pushed:
            if stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                stack.append(pushed.pop(0))
        
        while stack and stack[-1] == popped[j]:
            stack.pop()
            j += 1
        
        return j == len(popped)