class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {'}': '{', ']': '[', ')': '('}
        stack = []
        
        for c in s:
            if c == '{' or c == '[' or c== '(':
                stack.append(c)
            elif stack:
                element = stack.pop()
                if closeToOpen[c] != element:
                    return False
            else:
                return False
        if stack:
            return False
        return True
