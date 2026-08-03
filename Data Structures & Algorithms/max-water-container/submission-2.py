class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Logic: initialize a left and right pointer. At each iteration, keep track of which side is smaller, and move that pointer accordingly. Keep track of the max.
        maxV = 0
        l = 0
        r = len(heights) - 1
        while (l < r):
            volume = min(heights[l], heights[r]) * (r - l)
            maxV = max(volume, maxV)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxV
            
