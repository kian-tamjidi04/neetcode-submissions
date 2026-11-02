class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            sortedString = "".join(sorted(s))

            if sortedString not in anagrams:
                anagrams[sortedString] = [s]
            else:
                anagrams[sortedString].append(s)
        
        return list(anagrams.values())