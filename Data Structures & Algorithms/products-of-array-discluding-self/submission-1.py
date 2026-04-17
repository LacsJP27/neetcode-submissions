class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        product = 1
        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                product *= nums[i - 1]
                prefix.append(product)
        product = 1
        postfix = [0] * len(nums)
        for i in reversed(range(len(nums))):
            if i == len(nums) - 1:
                postfix[i] = prefix[i]
            else:
                product *= nums[i + 1]
                postfix[i] = prefix[i] * product
        
        return postfix

            
