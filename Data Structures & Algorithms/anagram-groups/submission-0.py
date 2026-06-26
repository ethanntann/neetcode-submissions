class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedDict = {} # string : []
        for s in strs:
            sorted_string = "".join(sorted(s))
            if sorted_string not in sortedDict:
                sortedDict[sorted_string] = []
            sortedDict[sorted_string].append(s) # [act, pots, pots, act, pots,hat]

        return list(sortedDict.values())