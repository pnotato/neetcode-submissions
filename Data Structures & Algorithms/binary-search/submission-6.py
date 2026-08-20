class Solution:
    # we're using pointers here instead of splicing becomes splicing is O(n)?
    def binary_search(self, l: int, r:int, nums: List[int], target: int) -> int:
        if l > r:
            return -1 
        midpoint = (l + r) // 2
        if target < nums[midpoint]:
            return self.binary_search(l, midpoint-1, nums, target)
        elif target > nums[midpoint]:
            return self.binary_search(midpoint+1, r, nums, target)
        else:
            return midpoint

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums)-1, nums, target)
        