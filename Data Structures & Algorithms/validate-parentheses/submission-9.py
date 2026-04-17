class Solution:
    def isValid(self, s: str) -> bool:
        charStack = []
        closeToOpen = {}

        closeToOpen[')'] = '('
        closeToOpen[']'] = '['
        closeToOpen['}'] = '{'

        for c in s:
            if c == ')' or c == ']' or c == '}':
                if not charStack or charStack.pop() != closeToOpen[c]:
                    return False
            else:
                charStack.append(c)
        return not charStack

