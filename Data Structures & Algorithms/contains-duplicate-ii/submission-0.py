class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        sets = {}

        for i, val in enumerate(nums):
            if val in sets and abs(sets[val] - i) <= k:
                return True
            else:
                sets[val] = i

        return False
 
