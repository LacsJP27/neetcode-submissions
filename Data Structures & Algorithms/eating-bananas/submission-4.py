class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    

        # k = 1: [25,10,23,4] = 52 hrs > 4
        # k = 2: [13, 5, 12, 2] = 32 hrs > 4
        # k = 3: [9, 4, 8, 2] = 23 hrs > 4
        # k = 100: [1, 1, 1, 1] = 4 hrs >
        # k = 50: [1, 1, 1, 1] = 4 hrs
        # k = 25: []

        # 1 - 25
        # l = 1, r = 25
        # # k = 12: [3, 1, 2, 1] 7 hrs > 4
        # l = 12 + 1, r = 25, mid = 38 / 2 = 19
        # # k = 19: [2, 1, 2, 1] 6 hrs > 4
        # l = 20, r = 25, mid = 45 / 2 = 22
        # # k = 22: [2, 1, 2, 1] 6 > 4
        # l = 23, r = 25, mid = 48 / 2 = 24
        # # k = 24: [2, 1, 1, 1] 5 > 4
        # l = 25, r = 25, mid = 25
        # # k = 25: [1, 1, 1, 1] 4 == 4!


        # [1, 4, 3, 2] h = 100
        # k = 2: 1 + 2 + 3 + 2 = 8 < 100
        # k = 1: 


        res = max(piles)
        l, r = 1, max(piles)

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            if hours > h:
                l = k + 1
            else:
                res = k
                r = k - 1
        
        return res
