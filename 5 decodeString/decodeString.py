class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if s[i] == "]":
                stack.pop(-1)
                popped = ""
                str1 = ""
                while popped != "[":
                    popped = stack.pop(-1)
                    str1 = popped + str1
                # multiplier = stack.pop(-1)
                multiplier = stack.pop(-1)
                while multiplier.isnumeric():
                    if stack:
                        multiplier = stack.pop(-1) + multiplier
                        continue
                    break
                if not multiplier[0].isnumeric():
                    stack.append(multiplier[0])
                    multiplier = multiplier[1:len(multiplier)]
                decodeStr = int(multiplier) * str1[1:len(str1)]
                stack += list(decodeStr)
        return "".join(stack)
                
        
            
            
        