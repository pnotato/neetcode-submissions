class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = {}

        for n in nums:
            if n not in s:
                s[n] = 1
            else:
                s[n] += 1

            if s[n] > len(nums) / 2:
                return n