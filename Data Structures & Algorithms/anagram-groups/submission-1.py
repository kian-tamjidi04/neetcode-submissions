class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Need to have a dictionary
        # Index = map of letters -> instances
        # Value = list of strings with that map
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)
        
        return list(res.values())
            