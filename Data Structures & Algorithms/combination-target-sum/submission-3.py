class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # if sum > target we back track and try a lower number
        # if sum < target we take the highest value and add 
        # when we backtrack don't reuse numbers that we already used to add
        res = []
        nums.sort()
        # i that tells us what we can choose from nums
        # cur: what values we have added to current combination
        # total: the current sum
        def dfs(i, cur, total):
            # base case
            if total == target:
                # create copy because we continue to use current to do other combinations
                res.append(cur.copy())
                return
            # base case
            if i >= len(nums) or total > target:
                return
            
            # recursive step
            # append the nums[i]
            # this is where you read the array
            cur.append(nums[i])
            # add the num at i with total 
            dfs(i, cur, total + nums[i])
            # remove the current candidate (nums[i]) from current
            # so you don't get duplicates
            cur.pop()
            # now you will never use nums[i] in the other tree
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res