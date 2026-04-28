class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # goal sum for subset = total sum / 2
        # two decisions: either include num in sum or don't then move on
        # O(n * sum(nums)) time, O(sum(nums)) space

        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for summ in dp:
                if target in nextDP:
                    return True
                nextDP.add(summ)
                nextDP.add(summ + nums[i])
            dp = nextDP

        return True if target in dp else False