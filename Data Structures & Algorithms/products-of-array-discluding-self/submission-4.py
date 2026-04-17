class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        res = [1] * len(nums)
        product = 1
        for i in range(len(nums)):
            pre.append(product)
            product *= nums[i]
        # [1, 1, 2, 8]
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = pre[i] * product # pre[3] = 8 * 1 = 8. pre[2] = 2 * 6 = 12
            product *= nums[i] # 1st: 1 * 6 = 6
        return res

        
