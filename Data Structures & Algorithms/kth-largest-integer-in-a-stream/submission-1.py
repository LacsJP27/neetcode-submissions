class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        i, end = len(self.nums) - 1, len(self.nums) - self.k 
        
        while i > end:
            i -= 1

        return self.nums[i]

        
