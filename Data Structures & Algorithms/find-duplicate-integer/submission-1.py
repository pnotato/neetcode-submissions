class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # let's start with a hash set. Naive solution.
        counted = set()
        for i in nums:
            if i in counted:
                return i
            else:
                counted.add(i)

        return -1