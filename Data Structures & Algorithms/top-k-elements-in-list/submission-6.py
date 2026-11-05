class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {} # {2: 3} -> 3 occurrences of the number 2

        # Populates map with frequencies of each value
        for x in nums:
            freqMap[x] = 1 + freqMap.get(x, 0)

        countMap = [[] for i in range(len(nums) + 1)] # [[1], [3, 4]] -> 1 occurrence of 1, 2 occurrences of 3 and 4

        for val, occurrences in freqMap.items():
            countMap[occurrences].append(val)

        res = []
        for i in range(len(countMap) - 1, -1, -1):
            for v in countMap[i]:
                res.append(v)
                if k == 1:
                    return res

                k -= 1
            