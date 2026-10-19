class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp caching solution
        cache = [False]*len(nums)
        cache[0] = True
        for i in range(len(nums)):
            if not cache[i]:
                continue
            else:
                # this needs to be + 1 since we start jumping at the next index
                for j in range(1, nums[i]+1):
                    if i + j < len(nums):
                        cache[i + j] = True

        return cache[-1]

