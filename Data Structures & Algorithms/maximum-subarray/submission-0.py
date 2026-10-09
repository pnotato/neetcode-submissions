class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # we can use Kadane's algorithm for this
        maxSum = nums[0] # since we need to return something
        curSum = 0

        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(curSum, maxSum)

        return maxSum

