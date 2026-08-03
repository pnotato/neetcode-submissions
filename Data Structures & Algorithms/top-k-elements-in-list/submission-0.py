class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # bucket sort. Create an array(bucket) for each item in nums.

        for num in nums:
            count[num] = 1 + count.get(num, 0) # initialize your hashmap with the counts as the values
        for num, cnt in count.items(): # two variables, since we're dealing with a dictionary
            freq[cnt].append(num)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res