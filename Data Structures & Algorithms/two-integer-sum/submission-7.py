class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for index, number in enumerate(nums):
            indices[number] = index

        for index, number in enumerate(nums):
            check = target - number
            if check in nums and indices[check] != index:
                return [index, indices[check]]




# hash map solution: define all the indices in a dictionary to the number
# then, for each number, check if the target - number exists in the hashmap.
# != is for values. is not will check memory inequality, for line 9
