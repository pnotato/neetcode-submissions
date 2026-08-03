class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for index, number in enumerate(nums):
            indices[number] = index

        for index, number in enumerate(nums):
            check = target - number
            if check in indices and index != indices[check]:
                return [index, indices[check]]


# this way is correct because for nums = [5,5], the hash map looks like this:
# [5:0, 5:1], meaning pulling indices[5] will always output 0.

# hash map solution: define all the indices in a dictionary to the number
# then, for each number, check if the target - number exists in the hashmap.
# != is for values. is not will check memory inequality, for line 9
