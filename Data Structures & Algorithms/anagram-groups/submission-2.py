class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)

        for s in strs:
            ordArr = [0] * 26
            for c in s:
                ordArr[ord(c) - ord('a')] += 1
            
            anagramMap[tuple(ordArr)].append(s)

        res = []
        
        for words in anagramMap.values():
            res.append(words)
        
        return res