class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letterToWordsMap = defaultdict(list)

        for word in strs:
            letters = [0] * 26
            for c in word:
                letters[ord(c) - ord('a')] += 1

            letterToWordsMap[tuple(letters)].append(word)

        res = []

        for group in letterToWordsMap.values():
            res.append(group)
        
        return res
