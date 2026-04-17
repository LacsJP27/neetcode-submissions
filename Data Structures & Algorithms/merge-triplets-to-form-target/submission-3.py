class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # target
        # triplet lsit
        # can apply operations to get target:
            # maximize two triplets

        # check the triplets as is for the target
            # return true if already in the triplet
        # Then try maximizing every triplet combination
            # return whether one of these maximzed triplets == target
        # 
        
        # Maximize function
            # maximize two triplets
            # involves merging them too
            # TODO: not in place?
        # store maximized value
        # initialize maximizer with [0, 0, 0]
        def maximize(triplet1, triplet2):
            return ([max(triplet1[0], triplet2[0]), 
                max(triplet1[1], triplet2[1]), max(triplet1[2], triplet2[2])])

        tripMax = [0, 0, 0]

        for triplet in triplets:
            if target == triplet or target == tripMax:
                return True
            elif target[0] == triplet[0] or target[1] == triplet[1] or target[2] == triplet[2]:
                if max(target) >= max(triplet):
                     tripMax = maximize(tripMax, triplet)
               
            
        
        return target == tripMax
