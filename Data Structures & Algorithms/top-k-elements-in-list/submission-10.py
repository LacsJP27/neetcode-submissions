class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a hashmap to store counts of elements
        # sort the values in the maps
        # add the values to a result array until result size is k

        counts = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        for num, cnt in counts.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

