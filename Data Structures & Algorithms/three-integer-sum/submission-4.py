class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # logic: we can treat this as sorted two sum, with 
        # the first number, and finding two numbers equal to 
        # the negative of that number. 
        # since we cant have duplicates we start the window later.
        nums.sort()
        res_arr = []
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1
            while l < r:
                res = nums[l] + nums[r] + nums[i]
                if res > 0:
                    r -= 1
                elif res < 0:
                    l += 1
                else:
                    res_arr.append([nums[l], nums[r], nums[i]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            
        return res_arr
            



        