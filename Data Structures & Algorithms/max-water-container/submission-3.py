class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxV = 0
        l = 0
        r = len(heights) - 1

        while (r > l):
            vol = min(heights[r], heights[l]) * (r - l)
            maxV = max(maxV, vol)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1

        return maxV
            
            