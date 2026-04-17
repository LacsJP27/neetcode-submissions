class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # stores temp and index
        res = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # current temp t is greater than temp at top of stack
                stackT, stackI = stack.pop() # pop temp and index from top of stack
                res[stackI] = i - stackI # store the diff or num of days apart from the curr 
                                         # index where greater temp found and next smallest stack
                # repeat until the current temp is not greater than whatever is at the top of the stack

            stack.append((t, i))
        return res