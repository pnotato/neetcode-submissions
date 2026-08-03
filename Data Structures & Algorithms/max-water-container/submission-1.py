class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        l, r = 0, len(heights)-1

        while l < r:
            max_area = max(max_area, (r - l)*min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area


        # My implementation -- Brute Force
        # res = 0 

        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         tmp = min(heights[i], heights[j]) * (j - i)
        #         if tmp > res:
        #             res = tmp
        # return res
