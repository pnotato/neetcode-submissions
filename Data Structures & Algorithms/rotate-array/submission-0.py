class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotations = k % len(nums)
        nums[:] = nums[-rotations:] + nums[:-rotations]