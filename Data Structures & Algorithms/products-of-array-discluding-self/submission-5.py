class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = [1] * (len(nums))
        post = [1] * (len(nums))
        res = [1] * len(nums)
        product = 1

        for i in range(len(nums)):
            product *= nums[i]
            pre[i] = product

        product = 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                res[i] = pre[i - 1]
            elif i == 0:
                res[i] = product
            else:
                res[i] = pre[i - 1] * product
            
            product *= nums[i]


        return res

        
