class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            # break the second part of the array since they're gonna be duplicates
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums)-1
            while (l < r):
                curr = nums[l] + nums[r] + nums[i]
                if curr > 0:
                    r -= 1
                elif curr < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while (nums[l] == nums[l-1] and l < r):
                        l += 1
        return res