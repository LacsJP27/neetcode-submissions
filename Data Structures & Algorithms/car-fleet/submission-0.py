class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # create an array of pairs
        pair = [[p, s] for p, s in zip(position, speed)]

         # sort the array of pairs
        pair.sort(reverse = True)

        stack = []
        for p, s in pair:
            stack.append((target - p) / s)
            # if the time at the top of the stack is less than the time from the time below it
            # then they collide and combine
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


       

        



            



