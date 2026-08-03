class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            sortedStrings = "".join(sorted(string))
            # just using sorted will result in a list
            # join uses the "" as a seperator.
            res[sortedStrings].append(string)
        return list(res.values())
