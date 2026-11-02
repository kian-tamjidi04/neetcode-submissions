class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Can't be anagrams if lengths are unequal
        if len(s) != len(t):
            return False

        sMap = defaultdict()
        tMap = defaultdict()

        # Idea: Populate each map where index = letter, value = no. occurrences
        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
            tMap[t[i]] = 1 + tMap.get(t[i], 0)

        return sMap == tMap