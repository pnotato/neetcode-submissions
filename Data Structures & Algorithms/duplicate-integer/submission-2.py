class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         hashmap = []
         for item in nums:
            if item in hashmap:
                return True
            else:
                hashmap.append(item)
         return False