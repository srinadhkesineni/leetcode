class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for c in s:
            if c=="]":
                val=stack.pop()
                text=""
                while stack and not str(val).isnumeric():
                    text=val+text if val!="[" else text
                    val=stack.pop()
                number=val
                while stack and str(stack[-1]).isnumeric():
                    number=stack.pop()+number
                [stack.append(text) for _ in range(int(number))]
            else:
                stack.append(c)
        return "".join(stack)