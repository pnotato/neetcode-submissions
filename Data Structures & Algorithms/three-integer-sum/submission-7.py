class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       # review: for each item in the list, iterate through, then treat as a two sum II. To avoid duplicates, we will skip over duplicated indices
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1
            while (l < r):
                curr = nums[l] + nums[r] + nums[i]
                if curr < 0:
                    l += 1
                elif curr > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res

    