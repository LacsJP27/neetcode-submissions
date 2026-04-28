class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # goal sum for subset = total sum / 2
        # two decisions: either include num in sum or don't then move on
        # O(n * sum(nums)) time, O(sum(nums)) space

        if sum(nums) % 2 == 1:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp: # for all sums in dp add the next num but no dupes
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t) # copy everything from prev DP
            dp = nextDP
        return True if target in dp else False
            
        