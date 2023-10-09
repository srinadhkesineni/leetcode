class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        #brackets mapping
        b_m={ ')':'(',']':'[','}':'{' }

        for i in s:
            if i in b_m.values():
                stack.append(i)
            elif i in b_m.keys():
                if not stack or stack.pop()!=b_m[i]:
                    return False
        return not stack

       